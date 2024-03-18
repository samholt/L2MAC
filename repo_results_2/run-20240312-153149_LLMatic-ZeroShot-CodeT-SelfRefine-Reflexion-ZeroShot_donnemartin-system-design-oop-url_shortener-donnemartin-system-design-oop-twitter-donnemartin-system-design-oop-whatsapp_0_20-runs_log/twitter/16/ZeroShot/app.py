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
	email = data.get('email')
	password = data.get('password')
	user = users.get(email)
	if not user or not user.check_password(password):
		return jsonify({'message': 'Invalid email or password'}), 401
	return jsonify(user.to_dict()), 200

@app.route('/users/<email>', methods=['GET'])
def get_user(email):
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	return jsonify(user.to_dict()), 200

@app.route('/users/<email>', methods=['PUT'])
def update_user(email):
	data = request.get_json()
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.update(**data)
	return jsonify(user.to_dict()), 200

@app.route('/posts', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(**data)
	posts[post.id] = post
	return jsonify(post.to_dict()), 201

@app.route('/posts/<id>', methods=['GET'])
def get_post(id):
	post = posts.get(id)
	if not post:
		return jsonify({'message': 'Post not found'}), 404
	return jsonify(post.to_dict()), 200

@app.route('/posts/<id>', methods=['DELETE'])
def delete_post(id):
	post = posts.get(id)
	if not post:
		return jsonify({'message': 'Post not found'}), 404
	del posts[id]
	return jsonify({'message': 'Post deleted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
