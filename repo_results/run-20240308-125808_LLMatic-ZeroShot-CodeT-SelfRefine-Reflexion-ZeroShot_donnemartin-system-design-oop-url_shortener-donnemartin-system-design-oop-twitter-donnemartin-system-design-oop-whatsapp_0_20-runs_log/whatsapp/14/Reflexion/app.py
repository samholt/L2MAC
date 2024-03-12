from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
sessions = {}

@dataclass
class User:
	name: str
	email: str
	password: str

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user = User(name=data['name'], email=data['email'], password=data['password'])
	users[user.email] = user
	return jsonify({'message': 'User created'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		sessions[user.email] = 'Logged In'
		return jsonify({'message': 'Logged in'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
	app.run(debug=True)
