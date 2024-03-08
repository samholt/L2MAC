from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class User:
	id: int
	username: str
	password: str

users = {}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return {'id': user.id}, 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
	user = users.get(user_id)
	if not user:
		return {'error': 'User not found'}, 404
	return {'id': user.id, 'username': user.username}, 200
