from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime

app = Flask(__name__)

users = {}
posts = {}

SECRET_KEY = 'secret'

@dataclass
class User:
	username: str
	email: str
	password: str
	profile: dict

@dataclass
class Post:
	user: str
	content: str
	likes: int
	retweets: int
	replies: list

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(data['username'], data['email'], data['password'], {})
	users[data['username']] = new_user
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid username or password'}), 401
	token = jwt.encode({'user': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
	return jsonify({'token': token.decode('UTF-8')}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, SECRET_KEY)
		user = users.get(data['user'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	new_post = Post(user.username, data['content'], 0, 0, [])
	posts[len(posts)] = new_post
	return jsonify({'message': 'Posted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
