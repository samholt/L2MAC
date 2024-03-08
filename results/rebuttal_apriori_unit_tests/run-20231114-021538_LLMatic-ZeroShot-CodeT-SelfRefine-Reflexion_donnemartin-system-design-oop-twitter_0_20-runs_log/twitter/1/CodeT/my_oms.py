from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	email = data['email']
	password = data['password']
	if email in users:
		return jsonify({'message': 'User already exists'}), 400
	users[email] = {
		'username': username,
		'password': generate_password_hash(password, method='sha256'),
		'posts': []
	}
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data['email']
	password = data['password']
	if email not in users or not check_password_hash(users[email]['password'], password):
		return jsonify({'message': 'Invalid credentials'}), 400
	token = jwt.encode({'user': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token.decode('UTF-8')}), 200

if __name__ == '__main__':
	app.run(debug=True)
