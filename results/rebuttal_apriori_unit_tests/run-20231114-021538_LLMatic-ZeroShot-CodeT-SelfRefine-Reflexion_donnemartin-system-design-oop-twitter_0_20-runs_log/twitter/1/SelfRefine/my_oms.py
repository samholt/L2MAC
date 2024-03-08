from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if not data or 'username' not in data or 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing data'}), 400
	username = data['username']
	email = data['email']
	password = data['password']
	if email in users:
		return jsonify({'message': 'User already exists'}), 400
	users[email] = {
		'username': username,
		'password': generate_password_hash(password),
		'posts': []
	}
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if not data or 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing data'}), 400
	email = data['email']
	password = data['password']
	if email not in users or not check_password_hash(users[email]['password'], password):
		return jsonify({'message': 'Invalid credentials'}), 400
	token = jwt.encode({'user': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	if not data or 'email' not in data or 'content' not in data:
		return jsonify({'message': 'Missing data'}), 400
	email = data['email']
	content = data['content']
	if email not in users:
		return jsonify({'message': 'User not found'}), 400
	users[email]['posts'].append(content)
	return jsonify({'message': 'Posted successfully'}), 200

@app.route('/posts', methods=['GET'])
def get_posts():
	data = request.get_json()
	if not data or 'email' not in data:
		return jsonify({'message': 'Missing data'}), 400
	email = data['email']
	if email not in users:
		return jsonify({'message': 'User not found'}), 400
	return jsonify({'posts': users[email]['posts']}), 200

if __name__ == '__main__':
	app.run(debug=True)
