#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
FLASK_APP=app.py flask run

