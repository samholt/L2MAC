from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# Mock database
users = {}
posts = {}

@dataclass
class User:
	id: int
	username: str
	email: str
	password: str
	bio: str
	website: str
	location: str
	followers: list
	following: list

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	likes: int
	retweets: int
	replies: list

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if not data or 'username' not in data or 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Invalid request'}), 400
	new_user = User(len(users) + 1, data['username'], data['email'], data['password'], '', '', '', [], [])
	users[new_user.id] = new_user
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if not data or 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Invalid request'}), 400
	for user in users.values():
		if user.email == data['email'] and user.password == data['password']:
			token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
			return jsonify({'token': token.decode('UTF-8')}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
	app.run(debug=True)
