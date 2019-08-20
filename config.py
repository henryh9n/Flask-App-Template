#!/usr/bin/env python3

"""main config of the project"""

__version__ = '0.0.1'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2019, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Development"


import os


DEBUG = True
ENV = 'Development'
TESTING = True

APP_HOST = '0.0.0.0'
APP_PORT = '5001'

APP_ROOT = os.path.dirname(os.path.realpath(__file__))

DB_HOST = '0.0.0.0'
DB_PORT = '5432'
DB_NAME = ''
DB_USER = ''
DB_PWD = ''

SALT = ''
SECRET_KEY = ''

SERVICE_EMAIL = ''
SERVICE_EMAIL_PWD = ''
