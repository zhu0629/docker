# -*- coding: utf-8 -*-
SECRET_KEY = "b'f#ri$bp01j7@60o)pv!w=1r)9)__151()w_*g-t&w@p+=4y-8z'"
SERVICE_URL = "http://192.168.2.120/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub_db',
        'USER': 'seafile',
        'PASSWORD': '34a13182-d2ce-47bc-b1a0-af862443cef8',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'memcached:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
COMPRESS_CACHE_BACKEND = 'locmem'
TIME_ZONE = 'Asia/Shanghai'
FILE_SERVER_ROOT = "http://192.168.2.120/seafhttp"
OFFICE_CONVERTOR_ROOT = 'http://192.168.2.120:8089'
