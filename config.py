#!/usr/bin/env python3

"""Document description."""

__version__ = '0.0.1'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2018, hharutyunyan'
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
DB_NAME = 'sssinsurance'
DB_USER = 'hharutyunyan'
DB_PWD = 'k62bXQ'

SALT = 'Bm8&`Chq#6U.;=mkNCuzkq%H=yYFD~6]e,|{H*]~-|*0P-$h7za&a9GySY6%w!5s'
SECRET_KEY = 'J%pakLL&O.ruP7pL6S-$KaB-(G%G/T9XM[D~fbw+d+vNy9*x.0->}<FqTsUHdJYz'

SERVICE_EMAIL = 'info@sss.hharutyunyan.me'
SERVICE_EMAIL_PWD = 'test123'
