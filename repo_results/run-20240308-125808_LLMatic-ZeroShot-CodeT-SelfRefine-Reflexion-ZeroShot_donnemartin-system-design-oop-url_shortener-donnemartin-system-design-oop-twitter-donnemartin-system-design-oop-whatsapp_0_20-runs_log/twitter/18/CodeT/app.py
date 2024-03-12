from flask import Flask, request, jsonify
from user import User
from post import Post

app = Flask(__name__)

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
	user = users.get(data.get('email'))
	if user and user.password == data.get('password'):
		return jsonify(user.to_dict()), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/users/<email>', methods=['GET', 'PUT', 'DELETE'])
def user_operations(email):
	user = users.get(email)
	if request.method == 'GET':
		if user:
			return jsonify(user.to_dict()), 200
		return jsonify({'message': 'User not found'}), 404
	elif request.method == 'PUT':
		data = request.get_json()
		if user:
			user.update(**data)
			return jsonify(user.to_dict()), 200
		return jsonify({'message': 'User not found'}), 404
	elif request.method == 'DELETE':
		if user:
			del users[email]
			return jsonify({'message': 'User deleted'}), 200
		return jsonify({'message': 'User not found'}), 404

@app.route('/posts', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(**data)
	posts[post.id] = post
	return jsonify(post.to_dict()), 201

@app.route('/posts/<post_id>', methods=['GET', 'DELETE'])
def post_operations(post_id):
	post = posts.get(post_id)
	if request.method == 'GET':
		if post:
			return jsonify(post.to_dict()), 200
		return jsonify({'message': 'Post not found'}), 404
	elif request.method == 'DELETE':
		if post:
			del posts[post_id]
			return jsonify({'message': 'Post deleted'}), 200
		return jsonify({'message': 'Post not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
