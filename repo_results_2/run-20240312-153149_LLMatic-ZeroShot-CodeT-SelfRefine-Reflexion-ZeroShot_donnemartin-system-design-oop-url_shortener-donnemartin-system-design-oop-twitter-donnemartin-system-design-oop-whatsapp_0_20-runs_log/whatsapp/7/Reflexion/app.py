from flask import Flask, request
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

users = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = ''
	status_message: str = ''
	last_seen_status: str = 'everyone'
	blocked_contacts: List[str] = []

@dataclass
class Group:
	admin: str
	name: str
	members: List[str] = []

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return {'message': 'User registered successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return {'message': 'Login successful'}, 200
	return {'message': 'Invalid email or password'}, 401

if __name__ == '__main__':
	app.run(debug=True)
