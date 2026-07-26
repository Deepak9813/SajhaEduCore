#settings/development.py
from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*', '192.168.0.116', '192.168.0.114']

# Allow all frontend origins during development.
# Do not use this in production.
# CORS_ALLOW_ALL_ORIGINS = True

# Allow cookies (refresh_token) to be sent with requests.
CORS_ALLOW_CREDENTIALS = True


# Frontend URLs allowed to access backend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://192.168.18.247:5173",
]

DATABASES = { 
    "default": { 
        "ENGINE": config('DB_ENGINE'), 
        "NAME": config('DB_NAME'),
        "USER": config('DB_USER'),
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": config('DB_HOST'),
        "PORT": config('DB_PORT'),
    } 
}
