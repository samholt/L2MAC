from flask import Flask, request, jsonify
from user import User
from post import Post, Comment
from message import Message
from notification import Notification

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	if User.register(username, email, password):
		return jsonify({'message': 'User registered successfully'}), 201
	return jsonify({'message': 'User already exists'}), 400

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	token = User.authenticate(username, password)
	if token:
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	username = data.get('username')
	profile_picture = data.get('profile_picture')
	bio = data.get('bio')
	website_link = data.get('website_link')
	location = data.get('location')
	is_private = data.get('is_private')
	if User.update_profile(username, profile_picture, bio, website_link, location, is_private):
		return jsonify({'message': 'Profile updated successfully'}), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	username = data.get('username')
	user_to_follow = data.get('user_to_follow')
	if User.follow(username, user_to_follow):
		return jsonify({'message': 'User followed successfully'}), 200
	return jsonify({'message': 'Error following user'}), 400

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	username = data.get('username')
	user_to_unfollow = data.get('user_to_unfollow')
	if User.unfollow(username, user_to_unfollow):
		return jsonify({'message': 'User unfollowed successfully'}), 200
	return jsonify({'message': 'Error unfollowing user'}), 400

@app.route('/get_timeline', methods=['POST'])
def get_timeline():
	data = request.get_json()
	username = data.get('username')
	timeline_posts = User.get_timeline(username)
	if timeline_posts is not None:
		return jsonify({'timeline_posts': [post.__dict__ for post in timeline_posts]}), 200
	return jsonify({'message': 'Error getting timeline'}), 400

@app.route('/create_post', methods=['POST'])
def create_post():
	data = request.get_json()
	username = data.get('username')
	text = data.get('text')
	images = data.get('images')
	if Post.create_post(username, text, images):
		return jsonify({'message': 'Post created successfully'}), 201
	return jsonify({'message': 'Error creating post'}), 400

@app.route('/like_post', methods=['POST'])
def like_post():
	data = request.get_json()
	username = data.get('username')
	post_id = data.get('post_id')
	if Post.like_post(username, post_id):
		return jsonify({'message': 'Post liked successfully'}), 200
	return jsonify({'message': 'Error liking post'}), 400

@app.route('/retweet_post', methods=['POST'])
def retweet_post():
	data = request.get_json()
	username = data.get('username')
	post_id = data.get('post_id')
	if Post.retweet_post(username, post_id):
		return jsonify({'message': 'Post retweeted successfully'}), 200
	return jsonify({'message': 'Error retweeting post'}), 400

@app.route('/create_comment', methods=['POST'])
def create_comment():
	data = request.get_json()
	username = data.get('username')
	text = data.get('text')
	post_id = data.get('post_id')
	if Comment.create_comment(username, text, post_id):
		return jsonify({'message': 'Comment created successfully'}), 201
	return jsonify({'message': 'Error creating comment'}), 400

@app.route('/search_posts', methods=['POST'])
def search_posts():
	data = request.get_json()
	keyword = data.get('keyword')
	results = Post.search_posts(keyword)
	return jsonify({'results': [post.__dict__ for post in results]}), 200

@app.route('/filter_posts', methods=['POST'])
def filter_posts():
	data = request.get_json()
	filter_type = data.get('filter_type')
	filter_value = data.get('filter_value')
	results = Post.filter_posts(filter_type, filter_value)
	return jsonify({'results': [post.__dict__ for post in results]}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	sender = data.get('sender')
	receiver = data.get('receiver')
	text = data.get('text')
	if Message.send_message(sender, receiver, text):
		return jsonify({'message': 'Message sent successfully'}), 200
	return jsonify({'message': 'Error sending message'}), 400

@app.route('/block_user', methods=['POST'])
def block_user():
	data = request.get_json()
	sender = data.get('sender')
	user_to_block = data.get('user_to_block')
	if Message.block_user(sender, user_to_block):
		return jsonify({'message': 'User blocked successfully'}), 200
	return jsonify({'message': 'Error blocking user'}), 400

@app.route('/unblock_user', methods=['POST'])
def unblock_user():
	data = request.get_json()
	sender = data.get('sender')
	user_to_unblock = data.get('user_to_unblock')
	if Message.unblock_user(sender, user_to_unblock):
		return jsonify({'message': 'User unblocked successfully'}), 200
	return jsonify({'message': 'Error unblocking user'}), 400

@app.route('/create_notification', methods=['POST'])
def create_notification():
	data = request.get_json()
	username = data.get('username')
	text = data.get('text')
	trigger = data.get('trigger')
	if Notification.create_notification(username, text, trigger):
		return jsonify({'message': 'Notification created successfully'}), 200
	return jsonify({'message': 'Error creating notification'}), 400

@app.route('/get_trending_topics', methods=['GET'])
def get_trending_topics():
	trending_topics = Post.get_trending_topics()
	return jsonify({'trending_topics': trending_topics}), 200

@app.route('/recommend_users', methods=['POST'])
def recommend_users():
	data = request.get_json()
	username = data.get('username')
	recommended_users = User.recommend_users_to_follow(username)
	if recommended_users is not None:
		return jsonify({'recommended_users': recommended_users}), 200
	return jsonify({'message': 'Error getting recommendations'}), 400

if __name__ == '__main__':
	app.run(debug=True)
