from flask import Flask, request, jsonify
from models import User, Post
from utils import hash_password, verify_password

app = Flask(__name__)

users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	if not username or not email or not password:
		return jsonify({'message': 'Invalid data'}), 400
	if email in users:
		return jsonify({'message': 'User already exists'}), 400
	users[email] = User(id=len(users)+1, username=username, email=email, password=hash_password(password))
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	if not email or not password:
		return jsonify({'message': 'Invalid data'}), 400
	user = users.get(email)
	if not user or not verify_password(user.password, password):
		return jsonify({'message': 'Invalid credentials'}), 400
	return jsonify({'token': 'JWT_TOKEN'}), 200

@app.route('/profile/<int:user_id>', methods=['GET', 'PUT'])
def profile(user_id):
	user = next((user for user in users.values() if user.id == user_id), None)
	if request.method == 'GET':
		if not user:
			return jsonify({'message': 'User not found'}), 404
		return jsonify({'username': user.username, 'email': user.email, 'profile_picture': user.profile_picture, 'bio': user.bio, 'website': user.website, 'location': user.location}), 200
	elif request.method == 'PUT':
		data = request.get_json()
		if not user:
			return jsonify({'message': 'User not found'}), 404
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website = data.get('website', user.website)
		user.location = data.get('location', user.location)
		return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/posts', methods=['GET', 'POST'])
def posts_view():
	if request.method == 'GET':
		return jsonify([{'id': post.id, 'user_id': post.user_id, 'content': post.content, 'timestamp': post.timestamp} for post in posts.values()]), 200
	elif request.method == 'POST':
		data = request.get_json()
		user_id = data.get('user_id')
		content = data.get('content')
		if not user_id or not content:
			return jsonify({'message': 'Invalid data'}), 400
		user = next((user for user in users.values() if user.id == user_id), None)
		if not user:
			return jsonify({'message': 'User not found'}), 404
		posts[len(posts)+1] = Post(id=len(posts)+1, user_id=user_id, content=content, timestamp='timestamp')
		return jsonify({'message': 'Post created successfully'}), 200

@app.route('/post/<int:post_id>', methods=['GET', 'DELETE'])
def post_view(post_id):
	if request.method == 'GET':
		post = posts.get(post_id)
		if not post:
			return jsonify({'message': 'Post not found'}), 404
		return jsonify({'id': post.id, 'user_id': post.user_id, 'content': post.content, 'timestamp': post.timestamp}), 200
	elif request.method == 'DELETE':
		post = posts.get(post_id)
		if not post:
			return jsonify({'message': 'Post not found'}), 404
		del posts[post_id]
		return jsonify({'message': 'Post deleted successfully'}), 200
