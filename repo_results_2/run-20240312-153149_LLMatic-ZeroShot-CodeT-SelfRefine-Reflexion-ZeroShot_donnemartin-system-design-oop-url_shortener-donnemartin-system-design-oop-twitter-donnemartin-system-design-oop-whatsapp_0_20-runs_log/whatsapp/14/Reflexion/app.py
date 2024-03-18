from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}

@dataclass
class User:
	id: int
	email: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(id=len(users)+1, email=data['email'], password=data['password'])
	users[user.id] = user
	return jsonify({'id': user.id, 'email': user.email}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.email == data['email'] and user.password == data['password']:
			return jsonify({'id': user.id, 'email': user.email}), 200
	return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
	app.run(debug=True)
