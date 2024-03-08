from flask import Flask, request, jsonify
from dataclasses import dataclass, field
import jwt
import re

app = Flask(__name__)

mock_db = {}
post_db = {}
interaction_db = {}
follow_db = {}
post_id = 0
interaction_id = 0
follow_id = 0

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: str = field(default='')
	bio: str = field(default='')
	website_link: str = field(default='')
	location: str = field(default='')
	is_private: bool = field(default=False)

@dataclass
class Post:
	username: str
	text: str
	images: list = field(default_factory=list)

@dataclass
class Like:
	username: str
	post_id: int

@dataclass
class Retweet:
	username: str
	post_id: int

@dataclass
class Reply:
	username: str
	post_id: int
	text: str

@dataclass
class Follow:
	follower_username: str
	followed_username: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['username'], data['password'])
	mock_db[user.username] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and user.password == data['password']:
		token = jwt.encode({'username': user.username}, 'secret', algorithm='HS256')
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user:
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website_link = data.get('website_link', user.website_link)
		user.location = data.get('location', user.location)
		user.is_private = data.get('is_private', user.is_private)
		return jsonify({'message': 'Profile updated successfully'}), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/create_post', methods=['POST'])
def create_post():
	global post_id
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user:
		post = Post(user.username, data['text'], data.get('images', []))
		post_db[post_id] = post
		post_id += 1
		return jsonify({'message': 'Post created successfully', 'post_id': post_id-1}), 201
	return jsonify({'message': 'User not found'}), 404

@app.route('/delete_post', methods=['DELETE'])
def delete_post():
	data = request.get_json()
	if data['post_id'] in post_db:
		del post_db[data['post_id']]
		return jsonify({'message': 'Post deleted successfully'}), 200
	return jsonify({'message': 'Post not found'}), 404

@app.route('/like_post', methods=['POST'])
def like_post():
	global interaction_id
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and data['post_id'] in post_db:
		like = Like(user.username, data['post_id'])
		interaction_db[interaction_id] = like
		interaction_id += 1
		return jsonify({'message': 'Post liked successfully', 'interaction_id': interaction_id-1}), 201
	return jsonify({'message': 'User or post not found'}), 404

@app.route('/retweet_post', methods=['POST'])
def retweet_post():
	global interaction_id
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and data['post_id'] in post_db:
		retweet = Retweet(user.username, data['post_id'])
		interaction_db[interaction_id] = retweet
		interaction_id += 1
		return jsonify({'message': 'Post retweeted successfully', 'interaction_id': interaction_id-1}), 201
	return jsonify({'message': 'User or post not found'}), 404

@app.route('/reply_post', methods=['POST'])
def reply_post():
	global interaction_id
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and data['post_id'] in post_db:
		reply = Reply(user.username, data['post_id'], data['text'])
		interaction_db[interaction_id] = reply
		interaction_id += 1
		return jsonify({'message': 'Post replied successfully', 'interaction_id': interaction_id-1}), 201
	return jsonify({'message': 'User or post not found'}), 404

@app.route('/follow', methods=['POST'])
def follow():
	global follow_id
	data = request.get_json()
	follower = mock_db.get(data['follower_username'])
	followed = mock_db.get(data['followed_username'])
	if follower and followed:
		follow = Follow(follower.username, followed.username)
		follow_db[follow_id] = follow
		follow_id += 1
		return jsonify({'message': 'User followed successfully', 'follow_id': follow_id-1}), 201
	return jsonify({'message': 'User not found'}), 404

@app.route('/unfollow', methods=['DELETE'])
def unfollow():
	data = request.get_json()
	for follow_id, follow in list(follow_db.items()):
		if follow.follower_username == data['follower_username'] and follow.followed_username == data['followed_username']:
			del follow_db[follow_id]
			return jsonify({'message': 'User unfollowed successfully'}), 200
	return jsonify({'message': 'Follow not found'}), 404

@app.route('/timeline', methods=['GET'])
def timeline():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user:
		followed_users = [follow.followed_username for follow in follow_db.values() if follow.follower_username == user.username]
		timeline_posts = [post for post_id, post in post_db.items() if post.username in followed_users]
		return jsonify({'timeline_posts': timeline_posts}), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/search', methods=['GET'])
def search():
	data = request.get_json()
	keyword = data['keyword']
	results = {'users': [], 'posts': []}
	for username, user in mock_db.items():
		if keyword in username or keyword in user.bio:
			results['users'].append(username)
	for post_id, post in post_db.items():
		if keyword in post.text:
			results['posts'].append(post_id)
	return jsonify(results), 200

@app.route('/filter', methods=['GET'])
def filter():
	data = request.get_json()
	filter_type = data['filter_type']
	filter_value = data['filter_value']
	results = {'posts': []}
	if filter_type == 'hashtag':
		for post_id, post in post_db.items():
			if '#' + filter_value in post.text.split():
				results['posts'].append(post_id)
	elif filter_type == 'mention':
		for post_id, post in post_db.items():
			if '@' + filter_value in post.text.split():
				results['posts'].append(post_id)
	elif filter_type == 'trending':
		trending_hashtags = re.findall(r'#\w+', ' '.join(post.text for post in post_db.values()))
		trending_hashtags = sorted(trending_hashtags, key=trending_hashtags.count, reverse=True)
		if trending_hashtags:
			for post_id, post in post_db.items():
				if trending_hashtags[0] in post.text.split():
					results['posts'].append(post_id)
	return jsonify(results), 200

@app.route('/')
def home():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)
