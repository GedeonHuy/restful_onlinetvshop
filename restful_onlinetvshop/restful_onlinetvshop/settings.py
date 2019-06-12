"""
Django settings for your project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# This is where you set this file to become YOUR OWN PROJECT SETTING
PROJECT_NAME = 'restful_onlinetvshop'
# You'll also want to configure the STATIC FILES at the bottom of this file

# Set your Authentication User Model
AUTH_USER_MODEL = 'users.CustomUser'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ugdr-m-#%_6e)(ss=r&(7(zc3k5jibvge@4+pd+gyma)fop*w&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # DJANGO APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'contact_form',

    # DJANGO KERNEL
    'django_kernel',

    # FRONTEND APPS
    'frontend',

    # MY APPS
    'users',
    'brands',
    'products',
    'payments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = PROJECT_NAME + '.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        # With this setting, default django templates folder would be
        # in the root folder of your project
        'DIRS': [
            os.path.join(BASE_DIR, 'templates') # If you're building APIs then delete this
        ],

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

WSGI_APPLICATION = PROJECT_NAME + '.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # Using postgresql as default local db. Change this in production.
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restful_onlinetvshop_db',
        'USER': 'gideon',
        'PASSWORD': '0963722007@A',
        'HOST': '127.0.0.1',
        'PORT': '5432',
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

# The string between your HOST string and the file path of the static files
# inside the 'static' folder
STATIC_URL = '/static/'

# Set the default static folder as 'static' for all of your static files.
# If you don't want all apps to share one static folder, you can change or delete this
# Read more at https://docs.djangoproject.com/en/2.2/howto/static-files/#configuring-static-files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Media files setting(recommendedly for images or videos storage)
# The string between your HOST string and the file path of the media files
# inside the 'media' folder (which was set by MEDIA_ROOT var)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")