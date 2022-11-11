from .common import *

SECRET_KEY = 'django-insecure-daif6g*_aoct$es+e7px$40hyu-ppa90^lc7&+23wvp5q8hnt7'

DEBUG = True

ALLOWED_HOSTS = ['testserver', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'polls_db',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}