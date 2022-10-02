"""
Django settings for efesto project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
#from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(zi5^m4bm0p3_5250th38ir7_x+*9%1^&uyia7&rfq4vykdjsc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
]


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'navbar',
    'templates',
    'gallery',
    'project',
    'team',
    'services',
    'contact_us',
    'news',
    'efesto',
]

TRANSLATABLE_MODEL_MODULES = [
    "home.models", 
    "navbar.models", 
    "templates.models", 
    "gallery.models", 
    "project.models",
    "team.models",
    "services.models",
    "contact_us.models",
    "news.models",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'efesto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
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

WSGI_APPLICATION = 'efesto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'efesto',
        'USER': 'root',
        'PASSWORD': 'Elena2020+',
        'HOST': 'localhost',
        'PORT': '4081',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('it', gettext('Italian')),
    #('ge', _('German')),
    #('sp', _('Spanish')),
    #('fr', _('French')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

IS_MONOLINGUAL=False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/assets/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'assets'),
)
IMAGES_PATH = STATIC_URL+'images/'
STYLES_PATH = STATIC_URL+'styles/'

MARKERS_PATH = IMAGES_PATH+'markers/'
PROJECTS_PATH = IMAGES_PATH+'projects/'
PROJECT_GALLERY_PATH = IMAGES_PATH+'projectgallery/'
TYPEPROJECT_PATH = IMAGES_PATH+'typeprojects/'
TEAM_PATH = IMAGES_PATH+'team/'
SERVICES_PATH = IMAGES_PATH+'services/'
NEWS_PATH = IMAGES_PATH+'news/'

GMAPS_LINK = 'https://www.google.it/maps/place/'

ERROR_IMAGE = IMAGES_PATH+'error.png'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

