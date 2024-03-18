from flask import Flask, request, jsonify
from user import User

app = Flask(__name__)

users = []

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(len(users) + 1, data['email'], data['username'], data['password'])
	users.append(new_user)
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = next((x for x in users if x.username == data['username']), None)
	if user and user.check_password(data['password']):
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/profile/<username>', methods=['GET'])
def view_profile(username):
	user = next((x for x in users if x.username == username), None)
	if user:
		return jsonify({'username': user.username, 'profile_picture': user.profile_picture, 'bio': user.bio, 'website': user.website, 'location': user.location}), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/profile/edit', methods=['POST'])
def edit_profile():
	data = request.get_json()
	user = next((x for x in users if x.username == data['username']), None)
	if user and user.check_password(data['password']):
		user.edit_profile(data.get('profile_picture'), data.get('bio'), data.get('website'), data.get('location'))
		return jsonify({'message': 'Profile updated successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/follow/<int:user_id>', methods=['POST'])
def follow(user_id):
	data = request.get_json()
	user = next((x for x in users if x.id == data['id']), None)
	if user and user_id in User.users:
		user.follow(user_id)
		return jsonify({'message': 'Followed user successfully'}), 200
	return jsonify({'message': 'Invalid user id or user to follow not found'}), 401

@app.route('/unfollow/<int:user_id>', methods=['POST'])
def unfollow(user_id):
	data = request.get_json()
	user = next((x for x in users if x.id == data['id']), None)
	if user and user_id in User.users:
		user.unfollow(user_id)
		return jsonify({'message': 'Unfollowed user successfully'}), 200
	return jsonify({'message': 'Invalid user id or user to unfollow not found'}), 401


