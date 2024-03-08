from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import User, Post, Follow, Like, Retweet, Reply, Message, Notification

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

# Mock database
users = {}
posts = {}
follows = {}
likes = {}
retweets = {}
replies = {}
messages = {}
notifications = {}

@login_manager.user_loader
def load_user(user_id):
	return users.get(user_id)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(username=data['username'], email=data['email'], password_hash='', bio='', location='', website='', is_private=False)
	user.set_password(data['password'])
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.check_password(data['password']):
		login_user(user)
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/profile', methods=['GET', 'PUT'])
@login_required
def profile():
	if request.method == 'GET':
		return jsonify(current_user), 200
	elif request.method == 'PUT':
		data = request.get_json()
		current_user.bio = data.get('bio', current_user.bio)
		current_user.location = data.get('location', current_user.location)
		current_user.website = data.get('website', current_user.website)
		current_user.is_private = data.get('is_private', current_user.is_private)
		return jsonify({'message': 'Profile updated successfully'}), 200
