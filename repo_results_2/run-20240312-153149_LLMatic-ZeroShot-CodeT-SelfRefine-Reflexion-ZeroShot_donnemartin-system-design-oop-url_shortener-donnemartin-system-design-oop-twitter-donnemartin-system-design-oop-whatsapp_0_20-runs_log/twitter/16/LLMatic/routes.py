from flask import Blueprint, request
from models import User, Post, Message, users_db, posts_db, messages_db
import jwt

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	email = data['email']
	username = data['username']
	password = data['password']
	if email in users_db or any(user.username == username for user in users_db.values()):
		return {'message': 'Email or username already in use'}, 400
	user = User(email, username, password)
	users_db[email] = user
	return {'message': 'User registered successfully'}, 200

@app_routes.route('/authenticate', methods=['POST'])
def authenticate():
	data = request.get_json()
	email = data['email']
	password = data['password']
	user = users_db.get(email)
	if not user or user.password != password:
		return {'message': 'Invalid credentials'}, 400
	token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')
	return {'token': token}, 200

@app_routes.route('/profile', methods=['GET', 'PUT'])
def profile():
	token = request.headers.get('Authorization')
	if not token:
		return {'message': 'Missing token'}, 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return {'message': 'Invalid token'}, 401
	email = data['email']
	user = users_db.get(email)
	if request.method == 'GET':
		return {
			'email': user.email,
			'username': user.username,
			'profile_picture': user.profile_picture,
			'bio': user.bio,
			'website_link': user.website_link,
			'location': user.location
		}, 200
	elif request.method == 'PUT':
		data = request.get_json()
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website_link = data.get('website_link', user.website_link)
		user.location = data.get('location', user.location)
		return {'message': 'Profile updated successfully'}, 200

@app_routes.route('/post', methods=['POST'])
def create_post():
	token = request.headers.get('Authorization')
	if not token:
		return {'message': 'Missing token'}, 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return {'message': 'Invalid token'}, 401
	email = data['email']
	user = users_db.get(email)
	data = request.get_json()
	text = data['text']
	images = data['images']
	post = Post(text, images, user)
	posts_db[len(posts_db)] = post
	return {'message': 'Post created successfully'}, 200

@app_routes.route('/like', methods=['POST'])
def like_post():
	token = request.headers.get('Authorization')
	if not token:
		return {'message': 'Missing token'}, 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return {'message': 'Invalid token'}, 401
	email = data['email']
	user = users_db.get(email)
	data = request.get_json()
	post_id = data['post_id']
	post = posts_db.get(post_id)
	if not post:
		return {'message': 'Post not found'}, 404
	post.likes += 1
	return {'message': 'Post liked successfully'}, 200

@app_routes.route('/retweet', methods=['POST'])
def retweet_post():
	token = request.headers.get('Authorization')
	if not token:
		return {'message': 'Missing token'}, 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return {'message': 'Invalid token'}, 401
	email = data['email']
	user = users_db.get(email)
	data = request.get_json()
	post_id = data['post_id']
	post = posts_db.get(post_id)
	if not post:
		return {'message': 'Post not found'}, 404
	post.retweets += 1
	return {'message': 'Post retweeted successfully'}, 200

@app_routes.route('/reply', methods=['POST'])
def reply_to_post():
	token = request.headers.get('Authorization')
	if not token:
		return {'message': 'Missing token'}, 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return {'message': 'Invalid token'}, 401
	email = data['email']
	user = users_db.get(email)
	data = request.get_json()
	post_id = data['post_id']
	reply_text = data['reply_text']
	post = posts_db.get(post_id)
	if not post:
		return {'message': 'Post not found'}, 404
	post.replies.append({'user': user.username, 'reply_text': reply_text})
	return {'message': 'Reply posted successfully'}, 200

@app_routes.route('/search', methods=['GET'])
def search():
	keyword = request.args.get('keyword')
	results = [post for post in posts_db.values() if keyword in post.text]
	return {'results': [post.text for post in results]}, 200

@app_routes.route('/filter', methods=['GET'])
def filter():
	element = request.args.get('element')
	results = [post for post in posts_db.values() if element in post.text]
	return {'results': [post.text for post in results]}, 200

@app_routes.route('/follow', methods=['POST'])
def follow():
	token = request.headers.get('Authorization')
	if not token:
		return {'message': 'Missing token'}, 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return {'message': 'Invalid token'}, 401
	email = data['email']
	user = users_db.get(email)
	data = request.get_json()
	target_username = data['target_username']
	target_user = next((user for user in users_db.values() if user.username == target_username), None)
	if not target_user:
		return {'message': 'User not found'}, 404
	target_user.followers.append(user.username)
	return {'message': 'Followed user successfully'}, 200

@app_routes.route('/unfollow', methods=['POST'])
def unfollow():
	token = request.headers.get('Authorization')
	if not token:
		return {'message': 'Missing token'}, 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return {'message': 'Invalid token'}, 401
	email = data['email']
	user = users_db.get(email)
	data = request.get_json()
	target_username = data['target_username']
	target_user = next((user for user in users_db.values() if user.username == target_username), None)
	if not target_user:
		return {'message': 'User not found'}, 404
	if user.username in target_user.followers:
		target_user.followers.remove(user.username)
	return {'message': 'Unfollowed user successfully'}, 200

@app_routes.route('/message', methods=['POST'])
def send_message():
	token = request.headers.get('Authorization')
	if not token:
		return {'message': 'Missing token'}, 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return {'message': 'Invalid token'}, 401
	email = data['email']
	sender = users_db.get(email)
	data = request.get_json()
	recipient_username = data['recipient_username']
	text = data['text']
	recipient = next((user for user in users_db.values() if user.username == recipient_username), None)
	if not recipient:
		return {'message': 'Recipient not found'}, 404
	message = Message(sender.username, recipient.username, text)
	messages_db[len(messages_db)] = message
	return {'message': 'Message sent successfully'}, 200

@app_routes.route('/notifications', methods=['GET'])
def get_notifications():
	token = request.headers.get('Authorization')
	if not token:
		return {'message': 'Missing token'}, 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return {'message': 'Invalid token'}, 401
	email = data['email']
	user = users_db.get(email)
	return {'notifications': user.notifications}, 200

@app_routes.route('/trending', methods=['GET'])
def trending_topics():
	# Mock implementation of trending topics
	# In a real-world application, this would involve complex algorithms
	# Here, we simply return the texts of the first 5 posts
	trending = [post.text for post in list(posts_db.values())[:5]]
	return {'trending': trending}, 200

@app_routes.route('/recommendations', methods=['GET'])
def user_recommendations():
	# Mock implementation of user recommendations
	# In a real-world application, this would involve complex algorithms
	# Here, we simply return the usernames of the first 5 users
	recommendations = [user.username for user in list(users_db.values())[:5]]
	return {'recommendations': recommendations}, 200
