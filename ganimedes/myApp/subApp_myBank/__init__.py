# app/subApp_myBank/__init__.py

from flask import Blueprint

myBank = Blueprint('myBank', __name__)

from . import routes
