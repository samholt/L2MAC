from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'

jwt = JWTManager(app)
db = SQLAlchemy(app)

from models import User, Post
from views import user_blueprint, post_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(post_blueprint)

if __name__ == '__main__':
	app.run(debug=True)
