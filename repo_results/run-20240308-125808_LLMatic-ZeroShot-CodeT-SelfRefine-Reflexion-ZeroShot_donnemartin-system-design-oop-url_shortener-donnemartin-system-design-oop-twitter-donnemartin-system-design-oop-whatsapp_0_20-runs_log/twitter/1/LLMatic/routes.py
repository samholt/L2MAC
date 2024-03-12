from flask import Flask, request
from models import User, Post, Message
import uuid

app = Flask(__name__)

# Mock database
users_db = {}
posts_db = {}
messages_db = {}
password_reset_tokens = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['username'], data['password'])
	users_db[data['email']] = user
	return {'message': 'User registered successfully'}, 201

@app.route('/auth', methods=['POST'])
def authenticate():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and user.password == data['password']:
		return {'token': 'JWT_TOKEN'}, 200
	else:
		return {'message': 'Invalid credentials'}, 401

@app.route('/password_reset', methods=['POST'])
def password_reset_request():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user:
		token = str(uuid.uuid4())
		password_reset_tokens[token] = user.email
		return {'token': token}, 200
	else:
		return {'message': 'User not found'}, 404

@app.route('/password_reset/<token>', methods=['POST'])
def password_reset(token):
	data = request.get_json()
	email = password_reset_tokens.get(token)
	if email:
		user = users_db.get(email)
		user.reset_password(data['new_password'])
		del password_reset_tokens[token]
		return {'message': 'Password reset successful'}, 200
	else:
		return {'message': 'Invalid token'}, 400

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and 'token' in data and data['token'] == 'JWT_TOKEN':
		user.update_profile(data.get('profile_picture'), data.get('bio'), data.get('website_link'), data.get('location'))
		return {'message': 'Profile updated successfully'}, 200
	else:
		return {'message': 'Invalid token or user not found'}, 401

@app.route('/create_post', methods=['POST'])
def create_post():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and 'token' in data and data['token'] == 'JWT_TOKEN':
		post = Post(data['text'], data['images'], user)
		post_id = str(uuid.uuid4())
		posts_db[post_id] = post
		return {'message': 'Post created successfully', 'post_id': post_id}, 201
	else:
		return {'message': 'Invalid token or user not found'}, 401

@app.route('/delete_post/<post_id>', methods=['DELETE'])
def delete_post(post_id):
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and 'token' in data and data['token'] == 'JWT_TOKEN' and post_id in posts_db and posts_db[post_id].user == user:
		del posts_db[post_id]
		return {'message': 'Post deleted successfully'}, 200
	else:
		return {'message': 'Invalid token, user not found, or unauthorized'}, 401

@app.route('/like_post/<post_id>', methods=['POST'])
def like_post(post_id):
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and 'token' in data and data['token'] == 'JWT_TOKEN' and post_id in posts_db:
		posts_db[post_id].like(user)
		return {'message': 'Post liked successfully'}, 200
	else:
		return {'message': 'Invalid token, user not found, or unauthorized'}, 401

@app.route('/retweet_post/<post_id>', methods=['POST'])
def retweet_post(post_id):
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and 'token' in data and data['token'] == 'JWT_TOKEN' and post_id in posts_db:
		posts_db[post_id].retweet(user)
		return {'message': 'Post retweeted successfully'}, 200
	else:
		return {'message': 'Invalid token, user not found, or unauthorized'}, 401

@app.route('/reply_post/<post_id>', methods=['POST'])
def reply_post(post_id):
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and 'token' in data and data['token'] == 'JWT_TOKEN' and post_id in posts_db and 'text' in data:
		posts_db[post_id].reply(user, data['text'])
		return {'message': 'Reply posted successfully'}, 200
	else:
		return {'message': 'Invalid token, user not found, unauthorized, or missing text'}, 401

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	user = users_db.get(data['email'])
	target_user = users_db.get(data['target_email'])
	if user and target_user and 'token' in data and data['token'] == 'JWT_TOKEN':
		user.follow(target_user)
		return {'message': 'User followed successfully'}, 200
	else:
		return {'message': 'Invalid token, user not found, or unauthorized'}, 401

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	user = users_db.get(data['email'])
	target_user = users_db.get(data['target_email'])
	if user and target_user and 'token' in data and data['token'] == 'JWT_TOKEN':
		user.unfollow(target_user)
		return {'message': 'User unfollowed successfully'}, 200
	else:
		return {'message': 'Invalid token, user not found, or unauthorized'}, 401

@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('q')
	matching_users = [user for user in users_db.values() if query in user.username]
	matching_posts = [post for post in posts_db.values() if query in post.text]
	return {'users': [user.username for user in matching_users], 'posts': [post.text for post in matching_posts]}, 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	sender = users_db.get(data['sender_email'])
	receiver = users_db.get(data['receiver_email'])
	if sender and receiver and 'token' in data and data['token'] == 'JWT_TOKEN' and 'text' in data:
		message = Message(sender, receiver, data['text'])
		message_id = str(uuid.uuid4())
		messages_db[message_id] = message
		return {'message': 'Message sent successfully', 'message_id': message_id}, 201
	else:
		return {'message': 'Invalid token, user not found, unauthorized, or missing text'}, 401
