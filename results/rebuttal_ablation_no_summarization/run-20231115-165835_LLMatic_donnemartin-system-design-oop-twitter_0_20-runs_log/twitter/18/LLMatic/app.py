from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)

users = {}
profiles = {}

@dataclass
class User:
	email: str
	username: str
	password: str

@dataclass
class Profile:
	user: User
	first_name: str
	last_name: str
	bio: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(data['email'], data['username'], data['password'])
	users[data['email']] = new_user
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid credentials'}), 401
	token = jwt.encode({'user': user.email}, 'secret', algorithm='HS256')
	return jsonify({'token': token}), 200

@app.route('/password_reset', methods=['POST'])
def password_reset():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	exp = datetime.utcnow() + timedelta(minutes=30)
	token = jwt.encode({'user': user.email, 'exp': exp}, 'secret', algorithm='HS256')
	return jsonify({'token': token}), 200

@app.route('/confirm_password_reset', methods=['POST'])
def confirm_password_reset():
	data = request.get_json()
	try:
		decoded = jwt.decode(data['token'], 'secret', algorithms=['HS256'])
	except jwt.ExpiredSignatureError:
		return jsonify({'message': 'Token expired'}), 401
	except jwt.InvalidTokenError:
		return jsonify({'message': 'Invalid token'}), 401
	user = users.get(decoded['user'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.password = data['new_password']
	return jsonify({'message': 'Password updated successfully'}), 200

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	try:
		decoded = jwt.decode(data['token'], 'secret', algorithms=['HS256'])
	except jwt.ExpiredSignatureError:
		return jsonify({'message': 'Token expired'}), 401
	except jwt.InvalidTokenError:
		return jsonify({'message': 'Invalid token'}), 401
	user = users.get(decoded['user'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user_profile = Profile(user, data['first_name'], data['last_name'], data['bio'])
	profiles[user.email] = user_profile
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/')
def home():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)
