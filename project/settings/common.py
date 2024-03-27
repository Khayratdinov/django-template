import os
from pathlib import Path
import environ
import importlib

env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
PROJECT_DIR = ROOT_DIR / "project"
environ.Env.read_env(os.path.join(ROOT_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


#  Add SECRET_KEY to .env and delete it ⤵
SECRET_KEY = "1u_l2m)cay%%)jki^)6%)r$1)qyeh=%uljcs6k^4w0gj_*1ek%"
# SECRET_KEY = env("SECRET_KEY")


DEBUG = True
DEBUG_TOOLBAR = False

ALLOWED_HOSTS = ["*"]


# ========================== APPLICATION DEFINITION ========================== #


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = []

LOCAL_APPS = ["project.apps.core"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ROOT_DIR / "db.sqlite3",
    }
}


# ============================ PASSWORD VALIDATION =========================== #

# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# =========================== INTERNATIONALIZATION =========================== #

# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# =============================== STATIC FILES =============================== #
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = "/static/"

STATICFILES_DIRS = [str(PROJECT_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


MEDIA_ROOT = str(PROJECT_DIR / "media")
MEDIA_URL = "/media/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Check if the debug_toolbar package is installed
if importlib.util.find_spec("debug_toolbar"):
    # Import the debug_toolbar module and add it to the INSTALLED_APPS

    DEBUG_TOOLBAR = True

    import debug_toolbar

    INSTALLED_APPS.append("debug_toolbar")

    # Add debug_toolbar to the MIDDLEWARE
    MIDDLEWARE.insert(
        0,
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    )

    # Set INTERNAL_IPS to allow local access to the debug_toolbar
    INTERNAL_IPS = ["127.0.0.1"]
