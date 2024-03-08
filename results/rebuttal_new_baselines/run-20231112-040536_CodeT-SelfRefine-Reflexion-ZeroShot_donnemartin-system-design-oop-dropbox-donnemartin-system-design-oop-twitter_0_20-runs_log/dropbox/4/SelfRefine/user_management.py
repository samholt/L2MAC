from dataclasses import dataclass
from db import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(80))


def register(data):
	user = User(name=data['name'], email=data['email'], password=data['password'])
	db.session.add(user)
	db.session.commit()
	return {'message': 'User registered successfully'}, 201

def login(data):
	user = User.query.filter_by(email=data['email']).first()
	if user and user.password == data['password']:
		return {'message': 'Login successful'}, 200
	return {'message': 'Invalid email or password'}, 401

def forgot_password(data):
	user = User.query.filter_by(email=data['email']).first()
	if user:
		user.password = data['new_password']
		db.session.commit()
		return {'message': 'Password updated successfully'}, 200
	return {'message': 'User not found'}, 404

def get_profile():
	return {'message': 'Profile endpoint'}, 200

def update_profile(data):
	return {'message': 'Profile update endpoint'}, 200
