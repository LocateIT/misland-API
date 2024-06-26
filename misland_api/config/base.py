import os
from datetime import timedelta

def str_to_bool(value):
    if value is None:
        return False
    return value.lower() in ('true', '1', 't', 'y', 'yes')


SETTINGS = {
    'logging': {
        'level': 'INFO'
    },
    'service': {
        'port': 3000
    },
    'environment': {
        'ROLLBAR_SCRIPT_TOKEN': os.getenv('ROLLBAR_SCRIPT_TOKEN'),
        'ROLLBAR_SERVER_TOKEN': os.getenv('ROLLBAR_SERVER_TOKEN'),
        'EE_PRIVATE_KEY': os.getenv('EE_PRIVATE_KEY'),
        'EE_SERVICE_ACCOUNT': os.getenv('EE_SERVICE_ACCOUNT'),
        'EE_SERVICE_ACCOUNT_JSON': os.getenv('EE_SERVICE_ACCOUNT_JSON'),
        'API_URL': os.getenv('API_URL'),
        'API_ADMIN_EMAIL': os.getenv('API_ADMIN_EMAIL'),
        'API_PASSWORD': os.getenv('API_PASSWORD'),
        'EMAIL_USER':os.getenv('EMAIL_USER'),
        'EMAIL_PASSWORD':os.getenv('EMAIL_PASSWORD'),
        'EMAIL_SERVER':os.getenv('EMAIL_SERVER'),
        'EMAIL_PORT':os.getenv('EMAIL_PORT'),
        'EMAIL_USE_TLS':str_to_bool(os.getenv('EMAIL_USE_TLS', 'False')),
        'EMAIL_USE_SSL':str_to_bool(os.getenv('EMAIL_USE_SSL', 'True'))
    },
    'ROLES': ['ADMIN', 'USER'],
    'SQLALCHEMY_DATABASE_URI': 'postgresql://'+os.getenv('POSTGRES_USER')+':'+os.getenv('POSTGRES_PASSWORD')+'@'+os.getenv('DATABASE_PORT_5432_TCP_ADDR')+':'+os.getenv('DATABASE_PORT_5432_TCP_PORT')+'/'+os.getenv('POSTGRES_DB'),
    'SECRET_KEY': 'mysecret',
    'DOCKER_URL': os.getenv('DOCKER_URL'),
    'REGISTRY_URL': 'localhost:'+os.getenv('REGISTRY_PORT_5000_TCP_PORT', ''),
    'UPLOAD_FOLDER': '/tmp/scripts',
    'ALLOWED_EXTENSIONS': set(['tar.gz']),
    'JWT_AUTH_USERNAME_KEY': 'email',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_EXPIRATION_DELTA': timedelta(seconds=60*60*24),
    'SCRIPTS_FS': '/data/scripts',
    'CELERY_BROKER_URL': 'redis://'+os.getenv('REDIS_PORT_6379_TCP_ADDR')+':' + os.getenv('REDIS_PORT_6379_TCP_PORT'),
    'CELERY_RESULT_BACKEND':'redis://'+os.getenv('REDIS_PORT_6379_TCP_ADDR')+':' + os.getenv('REDIS_PORT_6379_TCP_PORT')
}
