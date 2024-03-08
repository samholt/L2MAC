from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	if not username or not email or not password:
		return jsonify({'message': 'Missing or invalid data'}), 400
	if email in users:
		return jsonify({'message': 'User already exists'}), 400
	users[email] = {
		'username': username,
		'password': generate_password_hash(password),
		'profile': {},
		'posts': [],
		'following': [],
		'followers': [],
		'messages': [],
		'notifications': []
	}
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	if not email or not password:
		return jsonify({'message': 'Missing or invalid data'}), 400
	if email not in users or not check_password_hash(users[email]['password'], password):
		return jsonify({'message': 'Invalid credentials'}), 400
	token = jwt.encode({'user': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token.decode('UTF-8')}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	email = data.get('email')
	content = data.get('content')
	if not email or not content:
		return jsonify({'message': 'Missing or invalid data'}), 400
	if email not in users:
		return jsonify({'message': 'User does not exist'}), 400
	users[email]['posts'].append(content)
	return jsonify({'message': 'Post created successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
