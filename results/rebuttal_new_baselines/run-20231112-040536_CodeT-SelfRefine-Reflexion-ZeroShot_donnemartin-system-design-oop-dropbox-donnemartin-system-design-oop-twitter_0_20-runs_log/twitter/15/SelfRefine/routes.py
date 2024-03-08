from flask import request, jsonify
from app import app, db
from models import User, Post
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if not data or 'username' not in data or 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Invalid request'}), 400
	if User.query.filter_by(username=data['username']).first() is not None:
		return jsonify({'message': 'Username already exists'}), 400
	if User.query.filter_by(email=data['email']).first() is not None:
		return jsonify({'message': 'Email already exists'}), 400
	new_user = User(username=data['username'], email=data['email'], password=data['password'])
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'User registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if not data or 'username' not in data or 'password' not in data:
		return jsonify({'message': 'Invalid request'}), 400
	user = User.query.filter_by(username=data['username']).first()
	if user is None:
		return jsonify({'message': 'Username does not exist'}), 400
	if not user.check_password(data['password']):
		return jsonify({'message': 'Invalid password'}), 400
	return jsonify({'access_token': user.get_token()}), 200


@app.route('/post', methods=['POST'])
@jwt_required

def create_post():
	data = request.get_json()
	if not data or 'content' not in data:
		return jsonify({'message': 'Invalid request'}), 400
	user_id = get_jwt_identity()
	if user_id is None:
		return jsonify({'message': 'Authentication is required to create a post'}), 401
	new_post = Post(content=data['content'], user_id=user_id)
	db.session.add(new_post)
	db.session.commit()
	return jsonify({'message': 'Post created successfully'}), 201
