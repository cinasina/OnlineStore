from OnlineStore.settings import *
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Site-Maps
SITE_ID = 1

STATICFILES_DIRS = [
    BASE_DIR / "static"]

STATIC_ROOT = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



