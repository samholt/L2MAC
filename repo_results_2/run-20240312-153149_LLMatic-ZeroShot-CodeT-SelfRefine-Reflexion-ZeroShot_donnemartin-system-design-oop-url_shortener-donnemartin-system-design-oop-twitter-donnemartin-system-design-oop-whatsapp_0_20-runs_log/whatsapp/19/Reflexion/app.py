from flask import Flask, request
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
	user = User(name=data['name'], email=data['email'], password=data['password'])
	users[user.email] = user
	return {'message': 'User registered successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return {'message': 'Logged in successfully'}, 200
	return {'message': 'Invalid email or password'}, 401

if __name__ == '__main__':
	app.run(debug=True)
