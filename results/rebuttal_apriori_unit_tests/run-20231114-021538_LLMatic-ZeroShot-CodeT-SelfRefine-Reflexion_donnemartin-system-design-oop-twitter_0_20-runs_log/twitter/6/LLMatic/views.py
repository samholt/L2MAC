from flask import Flask, request, jsonify
import jwt
from models import User

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(len(users) + 1, data['username'], data['email'], data['password'])
	users[data['email']] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.authenticate(data['password']):
		token = jwt.encode({'user_id': user.id}, 'secret', algorithm='HS256')
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
		user_id = decoded['user_id']
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = next((user for user in users.values() if user.id == user_id), None)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.update_profile(data.get('profile_picture'), data.get('bio'), data.get('website'), data.get('location'))
	return jsonify({'message': 'Profile updated successfully'}), 200
