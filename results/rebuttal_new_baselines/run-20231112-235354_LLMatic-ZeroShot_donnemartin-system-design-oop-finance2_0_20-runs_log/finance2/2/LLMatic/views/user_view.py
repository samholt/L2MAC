from flask import request, jsonify
from models.user import User


def register():
	data = request.get_json()
	user = User.create_user(data['name'], data['email'], data['password'])
	return jsonify({'message': 'User created successfully'}), 201

def login():
	data = request.get_json()
	user = User.authenticate(data['email'], data['password'])
	if user:
		return jsonify({'message': 'Logged in successfully'}), 200
	else:
		return jsonify({'message': 'Invalid credentials'}), 401

