from flask import Flask, request
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
	return {'message': 'User created successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or user.password != data['password']:
		return {'message': 'Invalid email or password'}, 401
	sessions[user.email] = 'Logged In'
	return {'message': 'Logged in successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
