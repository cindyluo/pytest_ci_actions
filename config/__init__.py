
import os

ENV = os.environ.get('ENV')

if ENV == 'production':
    from config.production import *
else:
    from config.staging import *

DB_HOST = os.environ.get('DB_HOST')
