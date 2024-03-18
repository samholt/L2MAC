from flask import Flask, request, jsonify
from dataclasses import dataclass
import uuid

app = Flask(__name__)

users = {}
sessions = {}

@dataclass
class User:
	id: str
	email: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(id=str(uuid.uuid4()), email=data['email'], password=data['password'])
	users[user.id] = user
	return jsonify({'id': user.id}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.email == data['email'] and user.password == data['password']:
			sessions[user.id] = 'Logged In'
			return jsonify({'message': 'Logged In', 'id': user.id}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
	app.run(debug=True)
