#!/usr/bin/env python3

"""Controllers for the project."""

__version__ = '0.1.0'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2018, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Production"

from flask import Blueprint, render_template

routes = Blueprint('routes', __name__, )


@routes.route('/', methods=['GET', 'POST'])
def home():
    """Render home page."""
    return render_template('index.html')
