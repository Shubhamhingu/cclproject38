from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

STRIPE_PUBLIC_KEY = 'pk_test_51IhFiiSJYEmWMyWPCZF42QUJFhjAlhrb6skdhbcyuHOFxj0qBJiWpvW8WIj91yrEgSiTaeZEBwnMMpFtCikwaUql00fsYoPIb9'   #config('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = 'sk_test_51IhFiiSJYEmWMyWP6eZrADOAeQoyNY4UaQNQ6RL0DxRSCnVobBPGzE12nTuU9QMJzSGsUL5Hoyn18geCFYDvG50c00hGsAE8OU'   #config('STRIPE_TEST_SECRET_KEY')
