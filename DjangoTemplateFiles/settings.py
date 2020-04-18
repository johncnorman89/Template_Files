#Development email#
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
DEFAULT_FROM_EMAIL = 'testing@example.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False 
EMAIL_PORT = 1025

#Deployment email#
EMAIL_BACKEND =  'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'johncnorman89@gmail.com'
EMAIL_HOST_PASSWORD = 'mygmail01'
EMAIL_USE_TLS = True 
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#Database#
try:
    import MySQLdb  # noqa: F401
except ImportError:
    import sqlite3

if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/crack-mariner-181107:us-central1:django-deploy-test',
            'NAME': 'JCEnterprises',
            'USER': 'slim102471', #INPUT INSTANCE USERNAME HERE
            'PASSWORD': 'myGCP01', #INPUT INSTANCE PASSWORD HERE
        }
    }
else:
    # Running locally so connect to either a local sqlite3 instance or connect to

    DATABASES = {
        'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
    }
		
#static files#
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'JCEnterprises/static'),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')		