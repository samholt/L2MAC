from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from dataclasses import dataclass
import pytest

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

# Mock database
users = {}
posts = {}

@dataclass
class User:
	username: str
	password: str
	email: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	email = data.get('email')
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	password_hash = generate_password_hash(password)
	users[username] = User(username, password_hash, email)
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users.get(username)
	if not user or not check_password_hash(user.password, password):
		return jsonify({'message': 'Invalid username or password'}), 401
	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token), 200

if __name__ == '__main__':
	app.run(debug=True)
