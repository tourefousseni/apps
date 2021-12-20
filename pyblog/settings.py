from pathlib import Path
# from django.contrib.gis.db.backends.XXX
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$s7p551k75n+3l2iuf*qv92xo+c0i5)@4&_^4ev%q&p%*x75bl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['143.198.60.181']
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Our the app
    'django.contrib.gis',
    'leaflet',
    'contacts',
    # 'bootstrap',
    'django_bootstrap_datetimepicker',
    'crispy_forms',
    'crispy_bootstrap5',
    'reportlab',
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'plateform',
        'USER': 'myprojectuser',
        'PASSWORD':'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# LEAFLET_CONFIG = {

# 'SPATIAL_EXTENT': (11.22, -4.16,  13.05,  -7.00),

# 'DEFAULT_CENTER': (13.22, -5.16),
# 'DEFAULT_ZOOM': 7,
# 'MIN_ZOOM': 3,
# 'MAX_ZOOM': 1,
# 'DEFAULT_PRECISION': 6,

# }

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'pyblog/static')]
FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)                    ]
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

#CONNECTOR TO GDAL
GDAL_LIBRARY_PATH = "/Applications/Postgres.app/Contents/Versions/10/lib/libgdal.dylib"
GEOS_LIBRARY_PATH = "/Applications/Postgres.app/Contents/Versions/10/lib/libgeos_c.dylib"