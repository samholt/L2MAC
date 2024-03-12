from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
blocked_contacts = {}

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

@app.route('/block', methods=['POST'])
def block():
	data = request.get_json()
	user_email = data['user_email']
	blocked_user_email = data['blocked_user_email']
	if user_email not in blocked_contacts:
		blocked_contacts[user_email] = []
	blocked_contacts[user_email].append(blocked_user_email)
	return jsonify({'message': 'User blocked successfully'}), 200

@app.route('/unblock', methods=['POST'])
def unblock():
	data = request.get_json()
	user_email = data['user_email']
	blocked_user_email = data['blocked_user_email']
	if user_email in blocked_contacts and blocked_user_email in blocked_contacts[user_email]:
		blocked_contacts[user_email].remove(blocked_user_email)
	return jsonify({'message': 'User unblocked successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
