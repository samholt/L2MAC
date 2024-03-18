from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

users = {}
sessions = {}

SECRET_KEY = 'secret'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	if email in users:
		return jsonify({'message': 'User already exists'}), 400
	hashed_password = generate_password_hash(password, method='sha256')
	users[email] = {'password': hashed_password}
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = users.get(email)
	if not user or not check_password_hash(user['password'], password):
		return jsonify({'message': 'Invalid credentials'}), 400
	token = jwt.encode({'user': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
	sessions[email] = token
	return jsonify({'token': token.decode('UTF-8')}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	email = data.get('email')
	if email in sessions:
		del sessions[email]
	return jsonify({'message': 'Logged out successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
