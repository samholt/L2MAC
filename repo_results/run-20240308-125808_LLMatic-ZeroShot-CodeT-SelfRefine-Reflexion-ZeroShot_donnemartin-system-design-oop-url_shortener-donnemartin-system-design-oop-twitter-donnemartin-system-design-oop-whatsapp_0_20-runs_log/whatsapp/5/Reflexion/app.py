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
	if 'email' not in data or 'password' not in data or 'name' not in data:
		return jsonify({'message': 'Missing data'}), 400
	if data['email'] in users:
		return jsonify({'message': 'User already exists'}), 400
	users[data['email']] = User(name=data['name'], email=data['email'], password=data['password'])
	return jsonify({'message': 'User created'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing data'}), 400
	if data['email'] not in users or users[data['email']].password != data['password']:
		return jsonify({'message': 'Invalid credentials'}), 401
	sessions[data['email']] = True
	return jsonify({'message': 'Logged in'}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	if 'email' not in data:
		return jsonify({'message': 'Missing data'}), 400
	if data['email'] not in sessions:
		return jsonify({'message': 'Not logged in'}), 401
	del sessions[data['email']]
	return jsonify({'message': 'Logged out'}), 200

if __name__ == '__main__':
	app.run(debug=True)
