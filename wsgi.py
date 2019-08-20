#!/usr/bin/env python3

"""The runner of the project."""

__version__ = '1.0.0'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2019, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Development"

from app import app as application

if __name__ == '__main__':
    application.run(
        host=application.config['APP_HOST'],
        port=int(application.config['APP_PORT'])
    )
