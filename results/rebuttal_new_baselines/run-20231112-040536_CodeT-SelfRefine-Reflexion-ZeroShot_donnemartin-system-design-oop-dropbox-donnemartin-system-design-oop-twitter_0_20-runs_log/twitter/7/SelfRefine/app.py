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
		return jsonify({'message': 'Username already exists'}), 400
	users[data['username']] = data
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['username'] not in users or users[data['username']]['password'] != data['password']:
		return jsonify({'message': 'Invalid username or password'}), 400
	token = jwt.encode({'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token.decode('UTF-8')}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	token = data['token']
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	username = decoded['user']
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	posts[username] = data['post']
	return jsonify({'message': 'Post created'}), 200

if __name__ == '__main__':
	app.run(debug=True)
