#!/bin/bash

cd "$(dirname "$0")/.."

if [ $# -ne 1 ]; then
    echo "Usage: $0 app_name"
    exit 1
fi


APP_NAME=$1
APP_DIR=project/apps/$APP_NAME

mkdir -p "$APP_DIR"

python manage.py startapp "$APP_NAME" "$APP_DIR"

APP_PATH="project.apps.$APP_NAME"
SETTINGS_FILE=project/settings/base.py
if ! grep -qxF "$APP_PATH" "$SETTINGS_FILE"; then
  sed -i "/^LOCAL_APPS = \[/s/\[/\[\'$APP_PATH\', /" "$SETTINGS_FILE"
fi

sed -i "s/name = '$APP_NAME'/name = '$APP_PATH'/" "$APP_DIR/apps.py"

echo "Created $APP_NAME app successfully!"