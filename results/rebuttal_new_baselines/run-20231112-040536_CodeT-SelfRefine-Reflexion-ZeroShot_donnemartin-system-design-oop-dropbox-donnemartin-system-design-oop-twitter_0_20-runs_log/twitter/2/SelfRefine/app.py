from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'

jwt = JWTManager(app)
db = SQLAlchemy(app)

from models import User, Post
from services import UserService, PostService

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'username' not in data or 'email' not in data or 'password' not in data:
		return jsonify(message='Missing data'), 400
	user = UserService.register(data)
	return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'username' not in data or 'password' not in data:
		return jsonify(message='Missing data'), 400
	user = UserService.login(data)
	if user:
		access_token = create_access_token(identity=user['username'])
		return jsonify(access_token=access_token), 200
	return jsonify(message='Invalid credentials'), 401

@app.route('/users/<username>', methods=['GET'])
@jwt_required

def get_user(username):
	user = UserService.get_user(username)
	return jsonify(user), 200

@app.route('/users/<username>', methods=['PUT'])
@jwt_required

def update_user(username):
	data = request.get_json()
	user = UserService.update_user(username, data)
	return jsonify(user), 200

@app.route('/posts', methods=['POST'])
@jwt_required

def create_post():
	data = request.get_json()
	if 'username' not in data or 'content' not in data:
		return jsonify(message='Missing data'), 400
	post = PostService.create_post(data)
	return jsonify(post), 201

@app.route('/posts/<post_id>', methods=['GET'])
@jwt_required

def get_post(post_id):
	post = PostService.get_post(post_id)
	return jsonify(post), 200

@app.route('/posts/<post_id>', methods=['DELETE'])
@jwt_required

def delete_post(post_id):
	PostService.delete_post(post_id)
	return jsonify(message='Post deleted'), 200

if __name__ == '__main__':
	app.run(debug=True)
