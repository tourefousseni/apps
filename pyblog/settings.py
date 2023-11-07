# coding: utf-8
from pathlib import Path
from django.contrib.messages import constants as messages
# from django.contrib.gis.db.backends.XXX
import os
from decouple import config, Csv
from django.contrib.gis import gdal


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY=config('My_SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG=config('My_DEBUG', cast=bool)
# ALLOWED_HOSTS=config('ALLOWED_HOSTS', cast=Csv())
# ALLOWED_HOSTS=config('My_ALLOWED_HOSTS', cast=Csv())
# ALLOWED_HOSTS=['*']
# os.environ['My_ALLOWED_HOSTS']= 'localhost'
# os.environ['My_DEBUG'] = 'False'
# config('My_DEBUG', cast=bool)
# False
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG',  cast=bool, default=False)
# ALLOWED_HOSTS = config('127.0.0.1', 'localhost')
# ALLOWED_HOSTS=["*"]
ALLOWED_HOSTS = []
# DEBUG = bool(os.environ.get('DEBUG', default=False))
# My_ALLOWED_HOSTS= ['127.0.0.1'] if DEBUG==False else [ ]

# Application definition
INSTALLED_APPS = [

    # Listings Apps
    'paypal.standard.ipn',
    'pages.apps.PagesConfig',
    'contacts.apps.ContactsConfig',
    'maps.apps.MapsConfig',
    'accounts.apps.AccountsConfig',
    'gestion.apps.GestionConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Our the app
    'django.contrib.gis',
    'leaflet',
    'fabric',

    # 'bootstrap module', #
    'django_bootstrap_datetimepicker',
    'crispy_forms',
    'crispy_bootstrap5',
    'reportlab',
    # 'geo-rest',
    'geopy',
    # 'osgeo',
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

ROOT_URLCONF = 'pyblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }

]


WSGI_APPLICATION = 'pyblog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2.5/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'  :  'django.contrib.gis.db.backends.postgis',
        'NAME'    :   config('BD_NAME'),
        'USER'    :   config('BD_USER'),
        'PASSWORD':   config('BD_PASSWORD'),
        'HOST'    :   config('BD_HOST'),
        'PORT'    :   config('BD_PORT'),
        # 'NAME':    'plateform',
        # 'USER':    'myprojectuser',
        # 'PASSWORD': 'password',
        # 'HOST':    'localhost',
        # 'PORT':    '5432',

    }

}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#SETTING FILES FOR USER
AUTH_USER_MODEL = "accounts.User"
#AUTOMATIC TO CREATE ID
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL       = '/static/'
MEDIA_URL        = '/media/'
MEDIA_ROOT       = os.path.join(BASE_DIR, 'media')
STATIC_ROOT      = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'pyblog/static')
]

FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

#CONNECTOR TO GDAL
# GDAL_LIBRARY_PATH = "/Applications/Postgres.app/Contents/Versions/12/lib/libgdal.dylib",
# GEOS_LIBRARY_PATH = "/Applications/Postgres.app/Contents/Versions/12/lib/libgeos.dylib"
# GDAL_LIBRARY_PATH = "/System/Volumes/Preboot/Cryptexes/OS/opt/homebrew/lib/libgdal.dylib"
# GEOS_LIBRARY_PATH = "/System/Volumes/Preboot/Cryptexes/OS/opt/homebrew/lib/libgeos_c.dylib"
GDAL_LIBRARY_PATH='/venv/lib/python3.9/site-packages/django/contrib/gis/gdal/libgdal.py'
# GEOS_LIBRARY_PATH='/venv/lib/python3.9/site-packages/django/contrib/gis/geos/libgeos.py'
Path ="/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/ctypes/__init__.py"
# Messages      /Users/apple/Library/Python/3.9/lib/python/site-packages/django/contrib/gis/geos
MESSAGE_TAGS = {
    messages.ERROR: 'danger',

}
PAYPAL_RECEIVER_EMAIL = 'tourefousseni1@gmail.com'
PAYPAL_TEST = True

LEAFLET_CONFIG = dict(DEFAULT_CENTER=(13.10, -4.30),
                      DEFAULT_ZOOM=3, MIN_ZOOM=8,
                      MAX_ZOOM=30, DEFAULT_PRECISION=6,
                      SCALE='both', MINIMAP=True, EPSG=4354, RESET_VIEW=True,NO_GLOBALS = False)