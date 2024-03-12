from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'User already exists'}), 400
	password_hash = generate_password_hash(data['password'])
	users[data['email']] = password_hash
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	password_hash = users.get(data['email'])
	if password_hash and check_password_hash(password_hash, data['password']):
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid email or password'}), 401

if __name__ == '__main__':
	app.run(debug=True)
