from flask import request, jsonify
from app import app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime


@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	hashed_password = generate_password_hash(password, method='sha256')
	# Mock database
	users = {}
	users[username] = {'username': username, 'email': email, 'password': hashed_password}
	return jsonify({'message': 'Registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	# Mock database
	users = {}
	if username in users and check_password_hash(users[username]['password'], password):
		token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
		return jsonify({'token': token.decode('UTF-8')}), 200
	return jsonify({'message': 'Invalid username or password'}), 401
