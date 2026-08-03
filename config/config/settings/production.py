# settings/production.py

from .base import *


# -----------------------------
# Security Settings
# -----------------------------

SECRET_KEY = config("SECRET_KEY")

DEBUG = False


# -----------------------------
# CORS & CSRF Settings
# -----------------------------

# Allow only trusted frontend domains to access this API.
# WARNING: Do not set this to True in production.
# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    # "https://sajhainfotech.com",  # React frontend domain
    # "https://admin.sajhainfotech.com",  # React admin dashboard domain (if exists)
]


# Allow cookies (refresh_token) to be sent with requests.
CORS_ALLOW_CREDENTIALS = True

# Trusted frontend origins for CSRF protection.
CSRF_TRUSTED_ORIGINS = [
    # "https://sajhaeducore.onrender.com",
    # "https://sajhainfotech.com",
    # "https://admin.sajhainfotech.com",
]


# -----------------------------
# Host Settings
# -----------------------------

# Django backend API domain.
ALLOWED_HOSTS = [
    "sajhaeducore.onrender.com",
    # "api.sajhainfotech.com",
]


# --------------------------------------------------------------------
# Cookie Security Settings (Production-specific settings)
# ---------------------------------------------------------------------

# CSRF cookie name.
CSRF_COOKIE_NAME = "csrftoken"

# Send cookies only over HTTPS.
CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_DOMAIN = "" # optional(Django already uses the current domain by default.)
SESSION_COOKIE_SECURE = True



# -----------------------------
# Database Settings
# -----------------------------

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}