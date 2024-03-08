from flask import Blueprint, request
from cloudsafe.models.user import User

class UserController:
	def register(name, email, password, profile_picture):
		User.register(name, email, password, profile_picture)
		return {'message': 'User registered successfully'}, 201

	def login(email, password):
		user = User.authenticate(email, password)
		if user:
			return {'message': 'User authenticated successfully'}, 200
		else:
			return {'message': 'Invalid email or password'}, 401

	def update_profile(email, password, name, new_password, profile_picture):
		user = User.authenticate(email, password)
		if user:
			user.update_profile(name, email, new_password, profile_picture)
			return {'message': 'Profile updated successfully'}, 200
		else:
			return {'message': 'Invalid email or password'}, 401

	def calculate_storage_used(email, password):
		user = User.authenticate(email, password)
		if user:
			user.calculate_storage_used()
			return {'storage_used': user.storage_used}, 200
		else:
			return {'message': 'Invalid email or password'}, 401

user_controller = Blueprint('user_controller', __name__)
user_controller_view = UserController()

@user_controller.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	return user_controller_view.register(data['name'], data['email'], data['password'], data['profile_picture'])

@user_controller.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	return user_controller_view.login(data['email'], data['password'])

@user_controller.route('/profile', methods=['PUT'])
def update_profile():
	data = request.get_json()
	return user_controller_view.update_profile(data['email'], data['password'], data['name'], data['new_password'], data['profile_picture'])

@user_controller.route('/storage', methods=['GET'])
def calculate_storage_used():
	data = request.get_json()
	return user_controller_view.calculate_storage_used(data['email'], data['password'])
