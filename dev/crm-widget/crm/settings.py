
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&1u1@wpg1y8rro8zmgi@%1fg%ju@fu$q^*%3tum&eds6a(!4zf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp',
    'crispy_forms',
    'widget_tweaks',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'webapp.middleware.GlobalExceptionHandlerMiddleware',
]

ROOT_URLCONF = 'crm.urls'

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

WSGI_APPLICATION = 'crm.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = { # sqlite
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3m2m',
    }
}

#DATABASES = { # mysql on 192.168.1.68  #updated 4.9.2024: all tables, all autth
#    "default": {
#        "ENGINE": "django.db.backends.mysql",
#        "NAME": "crm_db5",
#        "USER": "root",
#        "PASSWORD": "some_pass",
#        "HOST": "192.168.1.68",
#        "PORT": "3306",
#    }
#}

#DATABASES = { # mysql on kikkare.eu.pythonanywhere
#    "default": {
#        "ENGINE": "django.db.backends.mysql",
#        "NAME": "kikkare$default",
#        "USER": "kikkare",
#        "PASSWORD": "some_pass",
#        "HOST": "kikkare.mysql.eu.pythonanywhere-services.com",
#        "PORT": "3306",
#    }
#}

# "mysql+pymysql://meckic:MySQL!23@meckic.mysql.pythonanywhere-services.com:3306/meckic$shop-list"
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATIC_ROOT = "/home/kikkare/dev/crm/static"  # needed in pythonanywhere only!
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] # also media/ and images needs this! NOT in pythonanywhere!

#MEDIA_URL = 'media/'  # 'media' (w/o slash) in pythonanywhere!
MEDIA_ROOT = BASE_DIR / 'static' # not in pythonanywhere
#MEDIA_ROOT = "/home/kikkare/dev/crm/static/media" # needed in pythonanywhere only!

# in pythonanywhere web tab !!!:
# /static/	/home/kikkare/dev/crm/.venv/lib/python3.10/site-packages/django/contrib/admin/static	 
# /static/	/home/kikkare/dev/crm/static	 
# /media/	/home/kikkare/dev/crm/static/media/media
# media files are in .../media/media dir in paw!!!

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#to get https to work...:
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = False

SECURE_HSTS_SECONDS = 86400  # This one was set to 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SESSION_COOKIE_SECURE = False  #False tu run remotely on Pi4z
CSRF_COOKIE_SECURE = False    #False tu run remotely on Pi4Z

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
