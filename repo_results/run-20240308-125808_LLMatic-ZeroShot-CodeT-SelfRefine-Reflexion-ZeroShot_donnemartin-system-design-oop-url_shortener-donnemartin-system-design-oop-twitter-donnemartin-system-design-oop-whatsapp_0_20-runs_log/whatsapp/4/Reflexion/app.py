from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}

@dataclass
class User:
	name: str
	email: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	name = data['name']
	email = data['email']
	password = data['password']
	if email in users:
		return jsonify({'message': 'Email already exists.'}), 400
	users[email] = User(name, email, password)
	return jsonify({'message': 'User registered successfully.'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data['email']
	password = data['password']
	if email not in users or users[email].password != password:
		return jsonify({'message': 'Invalid email or password.'}), 401
	return jsonify({'message': 'Logged in successfully.'}), 200

if __name__ == '__main__':
	app.run(debug=True)
