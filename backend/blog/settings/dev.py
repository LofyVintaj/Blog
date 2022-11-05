from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    os.environ.get('SERVER_NAME')
]