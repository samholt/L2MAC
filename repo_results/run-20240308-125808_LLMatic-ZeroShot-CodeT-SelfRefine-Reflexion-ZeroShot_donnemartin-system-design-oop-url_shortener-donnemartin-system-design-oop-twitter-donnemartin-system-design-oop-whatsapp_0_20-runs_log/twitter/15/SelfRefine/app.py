from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# Mock database
users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['username'] in users:
		return jsonify({'message': 'User already exists'}), 400
	users[data['username']] = data
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
	users[data['username']].update(data)
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	if len(data['content']) > 280:
		return jsonify({'message': 'Post content exceeds the limit'}), 400
	posts[data['username']] = data
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/post', methods=['DELETE'])
def delete_post():
	data = request.get_json()
	del posts[data['username']]
	return jsonify({'message': 'Post deleted successfully'}), 200

@app.route('/follow', methods=['POST'])
def follow_user():
	data = request.get_json()
	users[data['username']]['following'].append(data['follow_username'])
	users[data['follow_username']]['followers'].append(data['username'])
	return jsonify({'message': 'Followed user successfully'}), 200

@app.route('/unfollow', methods=['POST'])
def unfollow_user():
	data = request.get_json()
	users[data['username']]['following'].remove(data['unfollow_username'])
	users[data['unfollow_username']]['followers'].remove(data['username'])
	return jsonify({'message': 'Unfollowed user successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
