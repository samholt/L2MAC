from flask import Flask, request
from dataclasses import dataclass
import json

app = Flask(__name__)

users = {}
sessions = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None
	contacts: list = None

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return {'message': 'User created successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = users.get(email)
	if not user or user.password != password:
		return {'message': 'Invalid email or password'}, 401
	sessions[email] = 'Logged In'
	return {'message': 'Logged in successfully'}, 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	email = data.get('email')
	sessions.pop(email, None)
	return {'message': 'Logged out successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
