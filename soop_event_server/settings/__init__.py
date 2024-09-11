from .base import *

SECRET_KEY = "django-insecure-$dl^qbfkt+=!#co%_app2!95(@!qnudp*4e*7)g@gbnt@1xxd="

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR_PATH / "db.sqlite3",
    }
}

STATIC_URL = "static/"
