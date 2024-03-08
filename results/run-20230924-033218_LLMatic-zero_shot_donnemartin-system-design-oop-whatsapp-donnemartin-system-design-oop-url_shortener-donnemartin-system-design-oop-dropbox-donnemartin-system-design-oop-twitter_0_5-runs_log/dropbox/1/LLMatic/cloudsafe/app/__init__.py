from flask import Flask
from cloudsafe.app.user_controller import user_blueprint
from cloudsafe.app.file_controller import file_blueprint
from cloudsafe.app.security_controller import security_blueprint

def create_app():
	app = Flask(__name__)
	app.register_blueprint(user_blueprint)
	app.register_blueprint(file_blueprint)
	app.register_blueprint(security_blueprint)
	return app
