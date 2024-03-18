from flask import Flask, request, jsonify
from user import User
from post import Post

app = Flask(__name__)

# Mock database
users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = users.get(email)
	if not user or not user.check_password(password):
		return jsonify({'message': 'Invalid email or password'}), 401
	return jsonify(user.to_dict()), 200

@app.route('/users/<email>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(email):
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	if request.method == 'GET':
		return jsonify(user.to_dict()), 200
	elif request.method == 'PUT':
		data = request.get_json()
		user.update(**data)
		return jsonify(user.to_dict()), 200
	elif request.method == 'DELETE':
		del users[email]
		return jsonify({'message': 'User deleted'}), 204

@app.route('/posts', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(**data)
	posts[post.id] = post
	return jsonify(post.to_dict()), 201

@app.route('/posts/<post_id>', methods=['GET', 'DELETE'])
def post_detail(post_id):
	post = posts.get(post_id)
	if not post:
		return jsonify({'message': 'Post not found'}), 404
	if request.method == 'GET':
		return jsonify(post.to_dict()), 200
	elif request.method == 'DELETE':
		del posts[post_id]
		return jsonify({'message': 'Post deleted'}), 204

if __name__ == '__main__':
	app.run(debug=True)
