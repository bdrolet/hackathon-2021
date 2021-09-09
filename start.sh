#!/bin/bash

python3 -m pip install -i https://pypi.org/simple -q -r requirements.txt

# sets the Flask app to app.routes
# Blueprint is registered in app/routes/__init__.py
export FLASK_APP=app.routes

# Starts the http server
flask run
