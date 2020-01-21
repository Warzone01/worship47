
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
# Online generator:
# https://www.miniwebtool.com/django-secret-key-generator/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

ACCOUNT_ACTIVATION_DAYS = 14

MEDIA_ROOT = ""

# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}
