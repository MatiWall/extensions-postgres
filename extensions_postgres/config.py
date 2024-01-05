import os

PORT = 5432
HOST = 'postgres.mw'

USER = 'postgres'
PASSWORD = 'postgres'

REQUIRED_ARGS = ['host', 'port', 'database', 'user', 'password']

_DEFAULT_CONFIG = {
    'host': HOST,
    'port': PORT,  # Usually 5432 for PostgreSQL
    'user': USER,
    'password': PASSWORD
}

_SYSTEM_VARIABLES = {
    'host': 'DATABASE_HOST',
    'port': 'DATABASE_PORT',
    'database': 'DATABASE_NAME',
    'user': 'DATABASE_USER',
    'password': 'DATABASE_PASSWORD'
}


def set_global_config(**kwargs):
    global _DEFAULT_CONFIG
    for key, value in kwargs.items():
        if key in _DEFAULT_CONFIG.keys():
            _DEFAULT_CONFIG[key] = value

def get_config():
    global _DEFAULT_CONFIG

    for key, value in _SYSTEM_VARIABLES.items():
        if os.environ.get(key):
            _DEFAULT_CONFIG[key] = os.environ.get(value)

    return _DEFAULT_CONFIG

