from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	db.init_app(app)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .profile import profile as profile_blueprint
	app.register_blueprint(profile_blueprint)

	from .contacts import contacts as contacts_blueprint
	app.register_blueprint(contacts_blueprint)

	from .groups import groups as groups_blueprint
	app.register_blueprint(groups_blueprint)

	from .chat import chat as chat_blueprint
	app.register_blueprint(chat_blueprint)

	from .status import status as status_blueprint
	app.register_blueprint(status_blueprint)

	from .web import web as web_blueprint
	app.register_blueprint(web_blueprint)

	from .connectivity import connectivity as connectivity_blueprint
	app.register_blueprint(connectivity_blueprint)

	from .feedback import feedback as feedback_blueprint
	app.register_blueprint(feedback_blueprint)

	return app
