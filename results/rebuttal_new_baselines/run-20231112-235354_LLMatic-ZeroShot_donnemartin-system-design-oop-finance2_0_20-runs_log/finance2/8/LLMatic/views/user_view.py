from flask import request, jsonify
from models.user import User


def register():
	data = request.get_json()
	user = User.create_user(data['name'], data['email'], data['password'])
	return jsonify({'message': 'User registered successfully', 'user': user.__dict__}), 201


def login():
	data = request.get_json()
	user = User.find_by_email(data['email'])
	if user and user.authenticate(data['email'], data['password']):
		return jsonify({'message': 'Logged in successfully'}), 200
	else:
		return jsonify({'message': 'Invalid email or password'}), 401
