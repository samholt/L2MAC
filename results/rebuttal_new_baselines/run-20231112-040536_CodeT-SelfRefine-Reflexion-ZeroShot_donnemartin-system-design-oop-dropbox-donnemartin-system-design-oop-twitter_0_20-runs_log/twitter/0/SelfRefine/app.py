from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['username'] in users:
		return jsonify({'message': 'User already exists'}), 400
	users[data['username']] = {
		'password': data['password'],
		'email': data['email'],
		'profile': {}
	}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['username'] not in users or users[data['username']]['password'] != data['password']:
		return jsonify({'message': 'Invalid username or password'}), 400
	token = jwt.encode({'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token}), 200

@app.route('/profile', methods=['PUT'])
def update_profile():
	data = request.get_json()
	username = jwt.decode(data['token'], app.config['SECRET_KEY'])['user']
	users[username]['profile'] = data['profile']
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	username = jwt.decode(data['token'], app.config['SECRET_KEY'])['user']
	posts[username] = posts.get(username, []) + [data['post']]
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/posts', methods=['GET'])
def get_posts():
	data = request.get_json()
	username = jwt.decode(data['token'], app.config['SECRET_KEY'])['user']
	return jsonify({'posts': posts.get(username, [])}), 200

if __name__ == '__main__':
	app.run(debug=True)
