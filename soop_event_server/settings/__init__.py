import environ
from socket import gethostname, gethostbyname

from .base import *

env = environ.Env(
    DEBUG=(bool, True),
    ALLOWED_HOSTS=(list, []),
)
environ.Env.read_env(BASE_DIR_PATH / ".env")

SECRET_KEY: str = env("SECRET_KEY")

DEBUG: bool = env("DEBUG")

ALLOWED_HOSTS: list[str] = [gethostbyname(gethostname())] + env("ALLOWED_HOSTS")

STATIC_ROOT = BASE_DIR_PATH / "static"
STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR_PATH / "media"
MEDIA_URL = "media/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR_PATH / "db.sqlite3",
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
