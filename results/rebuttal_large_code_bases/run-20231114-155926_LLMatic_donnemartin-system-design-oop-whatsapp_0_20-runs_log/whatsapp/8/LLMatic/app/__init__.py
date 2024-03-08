"""
This file initializes the Flask application and its extensions.
"""

from flask import Flask
from flask_socketio import SocketIO
from app.database import MockDatabase as db

socketio = SocketIO()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object('app.config')

	socketio.init_app(app)

	from app import views, models

	return app, socketio
