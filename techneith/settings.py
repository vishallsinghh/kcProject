import os

import dj_database_url

#import django_heroku
#from techneith.aws.conf import *


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8bo_zv9t7^1v8oto6jm04i*wiwg@+9k++zr&_f4ohwa!ozvxex'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['13.232.119.166', '127.0.0.1', 'ec2-13-232-119-166.ap-south-1.compute.amazonaws.com', 'techneith.com', 'www.techneith.com']
CORS_ALLOW_ALL_ORIGINS = True
#X_FRAME_OPTIONS = 'SAMEORIGIN'
# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'froala_editor',
    'django_social_share',
    # created apps
    'stripe_gateway',
    'pages',
    'products',
    'service',
    'rest_framework',
    'payments', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'techneith.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'techneith.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# django_heroku.settings(locals())

STRIPE_ENDPOINT_SECRET = 'whsec_g4w7MC9LiHD0Om5RQojfMqOMEZWQLKod'
STRIPE_PUBLISHABLE_KEY = 'pk_live_51MQCs1Go1SowCtA905HXGEvDyBwXueBy6NFeCqZJOtbEIaau28QbmsGK4I4smWKmzw5ND7c3u1YBx5Alx6c7KWkE00NdKpkjqg'
STRIPE_SECRET_KEY = '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'