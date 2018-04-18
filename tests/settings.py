import os

SECRET_KEY = 'roverdotcom'
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
]
ROOT_URLCONF = []


DATABASES = {
    'default': {
        'ENGINE': 'django_warlock.backend',
        'NAME': 'testdb',
        'USER': 'travis',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
