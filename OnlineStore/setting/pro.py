from OnlineStore.settings import *
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['cinasina.ir', 'www.cinasina.ir']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '###',
        'USER': '###',
        'PASSWORD': '###',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# Site-Maps
SITE_ID = 1

STATICFILES_DIRS = [
    BASE_DIR / "static"]

MEDIA_URL = '/media/'
STATIC_ROOT = '/home/cinasina/public_html/static'
MEDIA_ROOT = '/home/cinasina/public_html/media'

SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_CONTENT_TYPE_NOSNIFF = True

## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OFFLINE = True
