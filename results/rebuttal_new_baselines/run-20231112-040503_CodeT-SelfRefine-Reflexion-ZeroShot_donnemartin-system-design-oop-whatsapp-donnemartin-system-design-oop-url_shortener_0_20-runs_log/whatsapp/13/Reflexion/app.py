from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
messages = {}

@dataclass
class User:
	name: str
	email: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(name=data['name'], email=data['email'], password=data['password'])
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	messages[data['sender']] = data['message']
	return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/get_messages', methods=['GET'])
def get_messages():
	return jsonify(messages), 200

if __name__ == '__main__':
	app.run(debug=True)
