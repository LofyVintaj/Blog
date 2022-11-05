from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    os.environ.get('SERVER_NAME')
]