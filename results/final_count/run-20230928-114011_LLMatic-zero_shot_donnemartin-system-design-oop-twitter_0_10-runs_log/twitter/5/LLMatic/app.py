from flask import Flask, request, jsonify
from user import User

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['username'], data['password'])
	users[user.username] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.password == data['password']:
		return jsonify({'token': user.generate_auth_token()}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/reset_password', methods=['POST'])
def reset_password():
	data = request.get_json()
	user = users.get(data['username'])
	if user and user.password == data['old_password']:
		user.reset_password(data['new_password'])
		return jsonify({'message': 'Password reset successfully'}), 200
	return jsonify({'message': 'Invalid username or old password'}), 401

@app.route('/')
def home():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)

