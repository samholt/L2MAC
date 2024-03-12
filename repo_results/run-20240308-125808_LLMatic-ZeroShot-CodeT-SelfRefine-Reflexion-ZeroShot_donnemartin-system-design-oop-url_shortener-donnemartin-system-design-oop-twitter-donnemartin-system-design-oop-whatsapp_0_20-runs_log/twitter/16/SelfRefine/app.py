from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime

app = Flask(__name__)

# Mock database
users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data and 'username' in data and data['username'] in users:
		return jsonify({'message': 'User already exists'}), 400
	users[data['username']] = data
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data and 'username' in data and (data['username'] not in users or users[data['username']]['password'] != data['password']):
		return jsonify({'message': 'Invalid username or password'}), 400
	token = jwt.encode({'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token.decode('UTF-8')}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	if data and 'user' in data and (data['user'] not in users or 'text' not in data or len(data['text']) > 280):
		return jsonify({'message': 'Invalid post'}), 400
	posts[len(posts)] = {'user': data['user'], 'text': data['text']}
	return jsonify({'message': 'Post created successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
