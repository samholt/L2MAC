from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
posts = {}
comments = {}
likes = {}

@dataclass
class User:
	id: str
	username: str
	email: str
	password: str
	profile_picture: str = None
	bio: str = None
	website_link: str = None
	location: str = None
	is_private: bool = False

@dataclass
class Post:
	id: str
	user_id: str
	content: str
	image: str = None

@dataclass
class Comment:
	id: str
	post_id: str
	user_id: str
	content: str

@dataclass
class Like:
	id: str
	post_id: str
	user_id: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data.get('id'))
	if user and user.password == data.get('password'):
		return jsonify(user), 200
	return {'message': 'Invalid credentials'}, 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(**data)
	posts[post.id] = post
	return jsonify(post), 201

@app.route('/comment', methods=['POST'])
def comment():
	data = request.get_json()
	comment = Comment(**data)
	comments[comment.id] = comment
	return jsonify(comment), 201

@app.route('/like', methods=['POST'])
def like():
	data = request.get_json()
	like = Like(**data)
	likes[like.id] = like
	return jsonify(like), 201

if __name__ == '__main__':
	app.run(debug=True)
