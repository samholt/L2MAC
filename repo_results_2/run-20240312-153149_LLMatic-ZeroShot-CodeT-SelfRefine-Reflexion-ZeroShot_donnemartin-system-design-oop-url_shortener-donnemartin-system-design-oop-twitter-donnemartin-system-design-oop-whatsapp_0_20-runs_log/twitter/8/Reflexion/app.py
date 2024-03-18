from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	hashed_password = generate_password_hash(password, method='sha256')
	users[username] = {'password': hashed_password, 'email': email}
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users.get(username)
	if not user or not check_password_hash(user['password'], password):
		return jsonify({'message': 'Invalid username or password'}), 401
	token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token.decode('UTF-8')}), 200

if __name__ == '__main__':
	app.run(debug=True)