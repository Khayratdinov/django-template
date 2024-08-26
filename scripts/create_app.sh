#!/bin/bash

# Перейти в корневой каталог проекта

cd "$(dirname "$0")/.."

# Проверить, что указан ровно один аргумент

if [ $# -ne 1 ]; then
    echo "Usage: $0 app_name"
    exit 1
fi

APP_NAME=$1
APP_DIR="project/apps/$APP_NAME"

# Создать каталог приложения и необходимые подкаталоги

mkdir -p "$APP_DIR/migrations" "$APP_DIR/tests"

# Определить файлы для создания

FILES=(
    "__init__.py"
    "admin.py"
    "apps.py"
    "models.py"
    "serializers.py"
    "views.py"
    "urls.py"
)

# Создать необходимые файлы

for file in "${FILES[@]}"; do
    touch "$APP_DIR/$file"
done

# Создать __init__.py в папке migrations

touch "$APP_DIR/migrations/__init__.py"

# Сгенерировать файл apps.py
cat <<EOF > "$APP_DIR/apps.py"
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ${APP_NAME^}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.apps.$APP_NAME'
    verbose_name = _("$(echo "$APP_NAME" | sed -e 's/\b\(.\)/\u\1/g')")
EOF

# Сгенерировать файл models.py с заголовочным комментарием

cat <<EOF > "$APP_DIR/models.py"
"""
Models for $APP_NAME app.
"""

from django.db import models

EOF

# Сгенерировать файл urls.py с заголовочным комментарием

cat <<EOF > "$APP_DIR/urls.py"
"""
URL configuration for $APP_NAME app.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
]
EOF

# Сгенерировать файл views.py с заголовочным комментарием

cat <<EOF > "$APP_DIR/views.py"
"""
Views for $APP_NAME app.
"""

from django.shortcuts import render

EOF

# Сгенерировать файл admin.py с заголовочным комментарием

cat <<EOF > "$APP_DIR/admin.py"
"""
Admin configuration for $APP_NAME app.
"""

from django.contrib import admin

EOF

# Добавить приложение в конец массива LOCAL_APPS в settings, если оно еще не добавлено

APP_PATH="project.apps.$APP_NAME"
SETTINGS_FILE="project/settings/common.py"

if ! grep -qxF "'$APP_PATH'" "$SETTINGS_FILE"; then
  sed -i "/^LOCAL_APPS = \[/a\    '$APP_PATH'," "$SETTINGS_FILE"
fi

echo "Created $APP_NAME app successfully!"
