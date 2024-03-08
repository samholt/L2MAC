from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	db.init_app(app)

	from . import routes, file_routes, share_routes
	app.register_blueprint(routes.bp)
	app.register_blueprint(file_routes.file_bp)
	app.register_blueprint(share_routes.share_bp)

	return app
