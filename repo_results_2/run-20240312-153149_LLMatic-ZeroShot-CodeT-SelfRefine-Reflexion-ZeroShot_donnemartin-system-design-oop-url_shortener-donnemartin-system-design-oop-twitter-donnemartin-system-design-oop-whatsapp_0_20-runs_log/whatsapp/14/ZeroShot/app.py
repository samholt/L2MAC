from flask import Flask, request, jsonify
from dataclasses import dataclass
import user

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = user.User(data['email'], data['password'])
	user.users_db[new_user.email] = new_user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user_to_login = user.users_db.get(data['email'])
	if user_to_login and user_to_login.password == data['password']:
		return jsonify({'message': 'Logged in successfully'}), 200
	else:
		return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
	app.run(debug=True)
