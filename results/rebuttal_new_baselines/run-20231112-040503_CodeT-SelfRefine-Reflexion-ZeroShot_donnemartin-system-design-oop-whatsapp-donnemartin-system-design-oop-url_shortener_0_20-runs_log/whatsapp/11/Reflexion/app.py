from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

users = {}
sessions = {}

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	if username in users:
		return make_response('User already exists', 400)
	hashed_password = generate_password_hash(password, method='sha256')
	users[username] = {'password': hashed_password, 'email': email}
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username not in users or not check_password_hash(users[username]['password'], password):
		return make_response('Login failed', 401)
	if username in sessions:
		return make_response('User already logged in', 400)
	token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	sessions[username] = token
	return jsonify({'token': token.decode('UTF-8')}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	username = data.get('username')
	if username not in sessions:
		return make_response('User not logged in', 400)
	del sessions[username]
	return jsonify({'message': 'Logged out successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
