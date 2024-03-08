from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt

app = Flask(__name__)

mock_db = {}
post_db = {}

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: str = None
	bio: str = None
	website_link: str = None
	location: str = None
	visibility: str = 'public'
	following: list = []
	followers: list = []

@dataclass
class Post:
	content: str
	images: list
	user: str
	likes: int = 0
	retweets: int = 0
	replies: int = 0

@app.route('/')
def home():
	return 'Hello, World!'

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
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/profile', methods=['GET', 'PUT'])
def profile():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		username = data['username']
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = mock_db.get(username)
	if request.method == 'GET':
		return jsonify(user.__dict__), 200
	elif request.method == 'PUT':
		data = request.get_json()
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website_link = data.get('website_link', user.website_link)
		user.location = data.get('location', user.location)
		user.visibility = data.get('visibility', user.visibility)
		return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/follow', methods=['POST', 'DELETE'])
def follow():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		username = data['username']
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = mock_db.get(username)
	if request.method == 'POST':
		data = request.get_json()
		follow_username = data['follow']
		follow_user = mock_db.get(follow_username)
		if follow_user:
			user.following.append(follow_username)
			follow_user.followers.append(username)
			return jsonify({'message': 'Followed user successfully'}), 200
		else:
			return jsonify({'message': 'User to follow not found'}), 404
	elif request.method == 'DELETE':
		data = request.get_json()
		unfollow_username = data['unfollow']
		unfollow_user = mock_db.get(unfollow_username)
		if unfollow_user:
			user.following.remove(unfollow_username)
			unfollow_user.followers.remove(username)
			return jsonify({'message': 'Unfollowed user successfully'}), 200
		else:
			return jsonify({'message': 'User to unfollow not found'}), 404

@app.route('/timeline', methods=['GET'])
def timeline():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		username = data['username']
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = mock_db.get(username)
	timeline_posts = [post.__dict__ for post in post_db.values() if post.user in user.following]
	return jsonify(timeline_posts), 200

@app.route('/post', methods=['POST', 'DELETE', 'PUT'])
def post():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		username = data['username']
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = mock_db.get(username)
	if request.method == 'POST':
		data = request.get_json()
		post = Post(data['content'], data['images'], user.username)
		post_db[post.content] = post
		return jsonify({'message': 'Post created successfully'}), 201
	elif request.method == 'DELETE':
		data = request.get_json()
		post_db.pop(data['content'], None)
		return jsonify({'message': 'Post deleted successfully'}), 200
	elif request.method == 'PUT':
		data = request.get_json()
		post = post_db.get(data['content'])
		if post:
			post.likes = data.get('likes', post.likes)
			post.retweets = data.get('retweets', post.retweets)
			post.replies = data.get('replies', post.replies)
		return jsonify({'message': 'Post updated successfully'}), 200

@app.route('/search', methods=['GET'])
def search():
	keyword = request.args.get('keyword')
	results = {'users': [], 'posts': []}
	for username, user in mock_db.items():
		if keyword.lower() in user.username.lower():
			results['users'].append(user.__dict__)
	for content, post in post_db.items():
		if keyword.lower() in post.content.lower():
			results['posts'].append(post.__dict__)
	return jsonify(results), 200

@app.route('/filter', methods=['GET'])
def filter():
	options = request.args.get('options').split(',')
	results = {'posts': []}
	for content, post in post_db.items():
		if any(option.lower() in post.content.lower() for option in options):
			results['posts'].append(post.__dict__)
	return jsonify(results), 200

if __name__ == '__main__':
	app.run(debug=True)
