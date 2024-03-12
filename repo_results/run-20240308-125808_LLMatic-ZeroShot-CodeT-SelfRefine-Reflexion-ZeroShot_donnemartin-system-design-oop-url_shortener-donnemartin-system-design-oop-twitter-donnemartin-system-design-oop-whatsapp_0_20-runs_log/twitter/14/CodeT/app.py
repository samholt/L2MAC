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

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	email = data.get('email')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	post = Post(user.email, data.get('content'))
	posts[post.id] = post
	return jsonify(post.to_dict()), 201

@app.route('/post/<post_id>', methods=['DELETE'])
def delete_post(post_id):
	post = posts.get(post_id)
	if not post:
		return jsonify({'message': 'Post not found'}), 404
	del posts[post_id]
	return '', 204

if __name__ == '__main__':
	app.run(debug=True)
