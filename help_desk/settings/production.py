from ..base import *
import os

ALLOWED_HOSTS = ['localhost']
DEBUG = False
DATABASES = {'default': 
                { 
                    'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql'),
                    'NAME': os.environ.get('DB_NAME', 'help_desk_db'),
                    'USER': os.environ.get('DB_USER', 'user'),
                    'PASSWORD': os.environ.get('DB_PASSWORD', 'password'),
                    'HOST': os.environ.get('DB_HOST', 'localhost'),
                    'PORT': os.environ.get('DB_PORT', '5432'), 
                } 
            }


