#!/usr/bin/env python3

"""Initializing the application."""

__version__ = '1.0.0'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2018, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Production"

from flask import Flask, g, request, session, render_template
from app.lib.db import DB

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('config')

db = DB(app.config.get('DB_HOST'),
        app.config.get('DB_USER'),
        app.config.get('DB_PWD'),
        app.config.get('DB_NAME'))


from app.routes import routes

app.register_blueprint(routes)
