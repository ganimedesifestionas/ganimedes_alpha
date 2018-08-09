"""
Routes and views for the flask application.
"""
from .. python_debug_utilities.python_debug_utilities import *
from .. service_bus import * 
import json
from datetime import datetime
from flask import render_template
from flask import request, make_response, jsonify, redirect, url_for
from . import home

@home.route('/')
@home.route('/home')
def homepage():
    """Renders the home page."""
    return render_template(
        'home/index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@home.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'home/contact.html',
        title='ganimedes Contact',
        year=datetime.now().year,
        message='our contact page.'
    )

@home.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'home/about.html',
        title='About',
        year=datetime.now().year,
        message='ganimedes...application description page.'
    )
@home.route('/myBank')
def myBank():
    """Renders the about page."""
    return render_template(
        'myBank/myBank_home.html',
        title='myBank',
        year=datetime.now().year,
        message='myBank...application description page.'
    )

