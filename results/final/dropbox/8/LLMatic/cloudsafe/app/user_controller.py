from flask import Blueprint, request
from cloudsafe.app.user_service import UserService

user_blueprint = Blueprint('user', __name__)
user_service = UserService()

@user_blueprint.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	response = user_service.register_user(data['id'], data['name'], data['email'], data['password'], data['profile_picture'])
	return {'message': response}, 200

@user_blueprint.route('/login', methods=['POST'])
def login_user():
	data = request.get_json()
	response = user_service.login_user(data['email'], data['password'])
	return {'message': response}, 200

@user_blueprint.route('/change_password', methods=['PUT'])
def change_password():
	data = request.get_json()
	response = user_service.change_password(data['email'], data['old_password'], data['new_password'])
	return {'message': response}, 200

@user_blueprint.route('/update_profile_picture', methods=['PUT'])
def update_profile_picture():
	data = request.get_json()
	response = user_service.update_profile_picture(data['email'], data['new_profile_picture'])
	return {'message': response}, 200
