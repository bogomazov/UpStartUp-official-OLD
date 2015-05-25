"""
Django settings for upstartup project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b&5i=#%-!1#ivo$&a&!#k5za3nli%-wi#i!e1n!yjxc=-$0(ne'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'userprofile.UserProfile'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djangobower',
    'djangular',
    'compressor',
    'startup',
    'userprofile',
    'rest_framework',
)

BOWER_INSTALLED_APPS = (
    'angularjs',
    'jquery',
    'bootstrap',
    'angular-xeditable'
)
# AUTHENTICATION_BACKENDS = (
#     'emailusernames.backends.EmailAuthBackend',
#     # Uncomment the following to make Django tests pass:
#     # 'django.contrib.auth.backends.ModelBackend',
# )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
)

# AUTHENTICATION_BACKENDS = (
#     'emailusernames.backends.EmailAuthBackend',
#     # Uncomment the following to make Django tests pass:
#     # 'django.contrib.auth.backends.ModelBackend',
# )

ROOT_URLCONF = 'upstartup.urls'

WSGI_APPLICATION = 'upstartup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db_name',
#         'USER': 'db_user',
#         'PASSWORD': 'db_user_password',
#         'HOST': ''
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

BOWER_COMPONENTS_ROOT = os.path.join(STATIC_ROOT, 'libs')

# # STATIC_ROOT = os.path.join(BASE_DIR,'static')

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static/"),
# )
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.IsAdminUser'
    ],
    'PAGE_SIZE': 10,
}

COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'bogomazov1998@gmail.com'
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.yandex.ua'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'andrew@bogomazz.com'
EMAIL_HOST_PASSWORD = 'password1998'