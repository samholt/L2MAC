from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
posts = {}

@dataclass
class User:
	id: int
	username: str
	email: str
	password: str
	bio: str
	website: str
	location: str
	is_private: bool

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	image_url: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(user), 201

@app.route('/edit_profile', methods=['PUT'])
def edit_profile():
	data = request.get_json()
	user = users.get(data['id'])
	if not user:
		return {'message': 'User not found'}, 404
	user.bio = data.get('bio', user.bio)
	user.website = data.get('website', user.website)
	user.location = data.get('location', user.location)
	user.is_private = data.get('is_private', user.is_private)
	return jsonify(user), 200

@app.route('/create_post', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(**data)
	if len(post.content) > 280:
		return {'message': 'Post content exceeds 280 characters'}, 400
	posts[post.id] = post
	return jsonify(post), 201

@app.route('/delete_post', methods=['DELETE'])
def delete_post():
	data = request.get_json()
	post = posts.get(data['id'])
	if not post:
		return {'message': 'Post not found'}, 404
	del posts[post.id]
	return {'message': 'Post deleted'}, 200

if __name__ == '__main__':
	app.run(debug=True)
