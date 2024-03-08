from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'

jwt = JWTManager(app)
db = SQLAlchemy(app)

import models
import services

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	services.register_user(data)
	return {'message': 'User registered successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	access_token = services.authenticate_user(data)
	return {'access_token': access_token}, 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	services.create_post(data)
	return {'message': 'Post created successfully'}, 201

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	services.follow_user(data)
	return {'message': 'Followed user successfully'}, 200

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	services.unfollow_user(data)
	return {'message': 'Unfollowed user successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
