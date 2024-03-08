from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}

@dataclass
class User:
	name: str
	email: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if not data.get('email'):
		return jsonify({'message': 'Email is required'}), 400
	user = User(name=data.get('name'), email=data.get('email'), password=data.get('password'))
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
