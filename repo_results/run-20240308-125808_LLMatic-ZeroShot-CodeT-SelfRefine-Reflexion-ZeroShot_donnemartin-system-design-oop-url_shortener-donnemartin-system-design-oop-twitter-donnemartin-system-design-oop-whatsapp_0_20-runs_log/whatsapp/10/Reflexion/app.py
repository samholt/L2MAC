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

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'email' in data and 'password' in data and 'name' in data:
		if data['email'] not in users:
			users[data['email']] = User(name=data['name'], email=data['email'], password=data['password'])
			return jsonify({'status': 'success'}), 200
		else:
			return jsonify({'status': 'error', 'message': 'User already exists'}), 400
	else:
		return jsonify({'status': 'error', 'message': 'Invalid request'}), 400

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'email' in data and 'password' in data:
		if data['email'] in users and users[data['email']].password == data['password']:
			sessions[data['email']] = 'Logged In'
			return jsonify({'status': 'success'}), 200
		else:
			return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 400
	else:
		return jsonify({'status': 'error', 'message': 'Invalid request'}), 400

if __name__ == '__main__':
	app.run(debug=True)
