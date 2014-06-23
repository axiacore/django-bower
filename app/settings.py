#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '_*zjhswt9umayc3hl4(a3trs3fz+zgh9l@o^1(bo#%jl@t4jqu'
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEST_PROJECT_APPS = (
    'app',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Pipeline
    'pipeline',

    # Bower
    'djangobower',

) + TEST_PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'djangobower.finders.BowerFinder',
)

# Pipeline settings
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'

# Static 
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Bower
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'app/static')

# Pipeline
PIPELINE_CSS = {
    
    # Libraries
    'libraries': {
        'source_filenames': (   
            'bower_components/bootstrap/dist/css/bootstrap.css',
        ),
        'output_filename': 'css/libs.min.css',
    },

    # Base styles
    'base': {
        'source_filenames': (
            'css/cover.css',
        ),
        'output_filename': 'css/main.min.css',
    },
}

PIPELINE_JS = {
    
    # Libraries
    'libraries': {
        'source_filenames': (
            'bower_components/jquery/dist/jquery.js'
        ),
        'output_filename': 'js/libs.min.js',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
)

AXES_LOGIN_FAILURE_LIMIT = 10
AXES_USE_USER_AGENT = True
AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = '403.html'

