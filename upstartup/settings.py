import os
from config import *
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'b&5i=#%-!1#ivo$&a&!#k5za3nli%-wi#i!e1n!yjxc=-$0(ne'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'userprofile.UserProfile'
SOCIAL_AUTH_USER_MODEL = 'userprofile.UserProfile'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'djangobower',
    'djangular',
    'compressor',
    'startup',
    'userprofile',
    'rest_framework',
    'django_extensions',
    'werkzeug',
    'cities',
    # 'south',
    # 'social.apps.django_app.default',
    # 'social_auth',
    # 'rest_framework_swagger',
)
# SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'
BOWER_INSTALLED_APPS = (
    'angularjs',
    'jquery',
    'bootstrap',
    'angular-xeditable',
    'angular-animate',
    'angular-cookies',
    'angular-touch',
    'angular-sanitize',
    'angular-resource',
    'angular-route',
    'angular-mocks'
)

AUTHENTICATION_BACKENDS = (
    # 'social.backends.linkedin.LinkedinOAuth2',
    # 'social.backends.linkedin.LinkedinOAuth',
    # 'social.backends.facebook.FacebookOAuth2',
    # 'social.backends.facebook.FacebookAppOAuth2',


    'django.contrib.auth.backends.ModelBackend',
)


# Add email to requested authorizations.


SOCIAL_AUTH_PIPELINE = (
     'social.pipeline.social_auth.social_details',
     'social.pipeline.social_auth.social_uid',
     'social.pipeline.social_auth.auth_allowed',
     'social.pipeline.social_auth.social_user',
     'social.pipeline.user.get_username',
     'social.pipeline.social_auth.associate_by_email',
     'social.pipeline.user.create_user',
     'social.pipeline.social_auth.associate_user',
     'social.pipeline.social_auth.load_extra_data',
     'social.pipeline.user.user_details'
)

# LOGIN_URL          = '/login/'
# LOGIN_REDIRECT_URL = '/logged-in/'
# LOGIN_ERROR_URL    = '/login-error/'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'


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
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)


ROOT_URLCONF = 'upstartup.urls'

WSGI_APPLICATION = 'upstartup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'upstartup',
        'USER': 'db_admin',
        'PASSWORD': 'password1234',
        'HOST': 'localhost'
    }
}


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
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser'
    ],

    'PAGE_SIZE': 10,
}

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'localhost:3000'
)

CITIES_POSTAL_CODES = ['US', 'CA', 'UA']

COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'bogomazov1998@gmail.com'
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.yandex.ua'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'andrew@bogomazz.com'
EMAIL_HOST_PASSWORD = 'password1998'
