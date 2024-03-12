from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)

users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	email = data['email']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	password_hash = generate_password_hash(password)
	users[username] = {'email': email, 'password': password_hash}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	user = users[username]
	if not check_password_hash(user['password'], password):
		return jsonify({'message': 'Invalid password'}), 400
	token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token.decode('UTF-8')}), 200

@app.route('/profile', methods=['PUT'])
def update_profile():
	data = request.get_json()
	username = data['username']
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	users[username].update(data)
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	username = data['username']
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	post_id = len(posts) + 1
	posts[post_id] = {'user': username, 'content': data['content']}
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
	if post_id not in posts:
		return jsonify({'message': 'Post does not exist'}), 400
	del posts[post_id]
	return jsonify({'message': 'Post deleted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
