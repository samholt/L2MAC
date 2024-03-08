from flask import Blueprint, request, current_app

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users')
def get_users():
	return current_app.config['user_service'].get_users()

@user_routes.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	new_user = current_app.config['user_service'].register_user(data['name'], data['email'], data['password'])
	return new_user, 201

@user_routes.route('/login', methods=['POST'])
def login_user():
	data = request.get_json()
	user = current_app.config['user_service'].authenticate_user(data['email'], data['password'])
	if user:
		return user, 200
	else:
		return {'message': 'Invalid email or password'}, 401

@user_routes.route('/users/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
	user = current_app.config['user_service'].get_profile(user_id)
	if user:
		return user, 200
	else:
		return {'message': 'User not found'}, 404
