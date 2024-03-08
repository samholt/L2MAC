from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)

users = {}
sessions = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	email = data['email']
	password = generate_password_hash(data['password'], method='sha256')
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = {'username': username, 'email': email, 'password': password}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users or not check_password_hash(users[username]['password'], password):
		return jsonify({'message': 'Invalid username or password'}), 400
	token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	sessions[username] = token
	return jsonify({'token': token.decode('UTF-8')}), 200

if __name__ == '__main__':
	app.run(debug=True)
