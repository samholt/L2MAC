from flask import Blueprint, request, jsonify
from models import User
import jwt
import secrets

views = Blueprint('views', __name__)

users = {}
password_reset_tokens = {}

@views.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'User already exists'}), 400
	user = User(data['email'], data['username'], data['password'])
	users[data['email']] = user
	return jsonify({'message': 'User registered successfully'}), 200

@views.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or not user.check_password(data['password']):
		return jsonify({'message': 'Invalid credentials'}), 400
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	return jsonify({'token': token}), 200

@views.route('/password_reset_request', methods=['POST'])
def password_reset_request():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	token = secrets.token_urlsafe()
	password_reset_tokens[data['email']] = token
	return jsonify({'message': 'Password reset link sent', 'password_reset_link': data['email'] + token}), 200

@views.route('/password_reset', methods=['POST'])
def password_reset():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or password_reset_tokens.get(data['email']) != data['token']:
		return jsonify({'message': 'Invalid password reset link'}), 400
	user.reset_password(data['new_password'])
	del password_reset_tokens[data['email']]
	return jsonify({'message': 'Password reset successfully'}), 200

@views.route('/profile', methods=['GET'])
def get_profile():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	return jsonify({'email': user.email, 'username': user.username, 'profile_picture': user.profile_picture, 'bio': user.bio, 'website_link': user.website_link, 'location': user.location}), 200

@views.route('/profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.update_profile(data['profile_picture'], data['bio'], data['website_link'], data['location'])
	return jsonify({'message': 'Profile updated successfully', 'profile_picture': user.profile_picture, 'bio': user.bio, 'website_link': user.website_link, 'location': user.location}), 200
