from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# Mock database
users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['username'] in users:
		return jsonify({'message': 'User already exists'}), 400
	data['password'] = generate_password_hash(data['password'])
	users[data['username']] = data
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['username'] not in users or not check_password_hash(users[data['username']]['password'], data['password']):
		return jsonify({'message': 'Invalid username or password'}), 400
	token = jwt.encode({'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	if 'user' not in data or data['user'] not in users:
		return jsonify({'message': 'Invalid user'}), 400
	if len(data['content']) > 280:
		return jsonify({'message': 'Post content exceeds 280 characters'}), 400
	posts[len(posts)] = data
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/posts', methods=['GET'])
def get_posts():
	return jsonify(posts), 200

if __name__ == '__main__':
	app.run(debug=True)
