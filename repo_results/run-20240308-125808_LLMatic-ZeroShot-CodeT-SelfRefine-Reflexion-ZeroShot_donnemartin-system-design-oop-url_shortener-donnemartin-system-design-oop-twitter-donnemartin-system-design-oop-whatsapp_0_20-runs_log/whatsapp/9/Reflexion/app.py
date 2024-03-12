from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}

@dataclass
class User:
	email: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'User already exists'}), 400
	users[data['email']] = User(data['email'], data['password'])
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	# In a real application, we would send a password reset link to the user's email.
	# Here, we just return a mock reset link.
	return jsonify({'reset_link': f'http://example.com/reset_password?email={user.email}'}), 200

if __name__ == '__main__':
	app.run(debug=True)
