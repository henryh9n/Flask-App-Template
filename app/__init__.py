#!/usr/bin/env python3

"""Initializing the application."""

__version__ = '1.0.0'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2019, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Development"

from flask import Flask, render_template
from app.lib.db import DB

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('config')

db = DB(app.config.get('DB_HOST'),
        app.config.get('DB_USER'),
        app.config.get('DB_PWD'),
        app.config.get('DB_NAME'))


from app.routes import routes

app.register_blueprint(routes)

@app.errorhandler(404)
def page_not_found(e):
    """Handle the page for 404 error."""
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """Handle the page for internal error."""
    # TODO: Send email to developers and admins
    return render_template('errors/500.html'), 500
