from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from routes import routes


def create_app(test_config=None):
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SECRET_KEY'] = 'secret'

	if test_config is not None:
		app.config.update(test_config)

	jwt = JWTManager(app)
	db.init_app(app)
	app.register_blueprint(routes)

	return app


if __name__ == '__main__':
	app = create_app()
	app.run(debug=True)
