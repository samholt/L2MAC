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
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return jsonify(user.to_dict()), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/users/<email>', methods=['GET'])
def get_user(email):
	user = users.get(email)
	if user:
		return jsonify(user.to_dict()), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/users/<email>', methods=['PUT'])
def update_user(email):
	data = request.get_json()
	user = users.get(email)
	if user:
		user.update(**data)
		return jsonify(user.to_dict()), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/posts', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(**data)
	posts[post.id] = post
	return jsonify(post.to_dict()), 201

@app.route('/posts/<id>', methods=['GET'])
def get_post(id):
	post = posts.get(id)
	if post:
		return jsonify(post.to_dict()), 200
	return jsonify({'message': 'Post not found'}), 404

@app.route('/posts/<id>', methods=['DELETE'])
def delete_post(id):
	post = posts.get(id)
	if post:
		del posts[id]
		return jsonify({'message': 'Post deleted'}), 200
	return jsonify({'message': 'Post not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
