import os
from decouple import config, Csv
from settings.common_settings import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        # 'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'OPTIONS': {
            'client_encoding': 'UTF8',
    },
    }
}

STATIC_URL = '/static/static/'
MEDIA_URL ='/static/media/'

STATIC_ROOT = '/vol/web/media'
MEDIA_ROOT = '/vol/web/static'
