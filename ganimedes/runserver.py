# run.py

import os
from os import environ
from myApp import create_app
from flask import render_template
from flask import request


os.environ["FLASK_CONFIG"] = "sandbox"
#os.environ["FLASK_APP"] = "runserver.py"
config_name = os.getenv('FLASK_CONFIG')
print('@@@@ENV@@@',config_name)

# Example configuration
#ENVIRONMENT_DEBUG = os.environ.get("DEBUG", default=False)
#if ENVIRONMENT_DEBUG.lower() in ("f", "false"):
#    ENVIRONMENT_DEBUG = False
#DEBUG = ENVIRONMENT_DEBUG
#SECRET_KEY = os.environ.get("SECRET_KEY", default=None)
#if not SECRET_KEY:
#    raise ValueError("No secret key set for Flask application")

#config_name = 'sandbox'
app = create_app(config_name)

###############################################
@app.errorhandler(404)
def page_not_found(e):
    varPageName1 = str(request._get_current_object())
    return render_template('404.html'), 404
###############################################

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)