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
	username = data['username']
	email = data['email']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = {'email': email, 'password': password, 'profile': {}, 'posts': [], 'following': [], 'followers': [], 'notifications': []}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users:
		return jsonify({'message': 'User not found'}), 400
	elif users[username]['password'] != password:
		return jsonify({'message': 'Invalid password'}), 400
	token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token}), 200

if __name__ == '__main__':
	app.run(debug=True)
