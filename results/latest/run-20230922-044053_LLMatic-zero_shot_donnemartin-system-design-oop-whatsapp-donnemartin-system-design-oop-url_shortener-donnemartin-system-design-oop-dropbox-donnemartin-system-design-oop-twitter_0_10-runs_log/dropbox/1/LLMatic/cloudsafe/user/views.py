from flask import request, jsonify
from .models import User
from cloudsafe.database import Database  # hypothetical Database class

db = Database('cloudsafe_db')  # provide the missing argument

def register():
	data = request.get_json()
	user = User(data['name'], data['email'], data['password'])
	db.save_user(user)  # Save the user to the database
	return jsonify({'message': 'User registered successfully'}), 201

def login():
	data = request.get_json()
	user = db.get_user_by_email(data['email'])  # Retrieve the user from the database
	if user and user.check_password(data['password']):
		# Log the user in
		return jsonify({'message': 'Login successful'}), 200
	else:
		return jsonify({'message': 'Invalid email or password'}), 401

def update_profile():
	data = request.get_json()
	user = db.get_current_user()  # Retrieve the current user from the database
	user.update_profile(data.get('name'), data.get('email'), data.get('password'), data.get('profile_picture'))
	db.save_user(user)  # Save the updated user to the database
	return jsonify({'message': 'Profile updated successfully'}), 200
