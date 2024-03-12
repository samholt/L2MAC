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
	return {'message': 'Invalid credentials'}, 401

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(**data)
	posts[post.id] = post
	return jsonify(post.to_dict()), 201

@app.route('/post/<post_id>', methods=['GET'])
def get_post(post_id):
	post = posts.get(post_id)
	if post:
		return jsonify(post.to_dict()), 200
	return {'message': 'Post not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
