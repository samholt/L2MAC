from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}

@dataclass
class User:
	email: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'User already exists'}), 400
	users[data['email']] = User(data['email'], data['password'])
	return jsonify({'message': 'User registered successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
