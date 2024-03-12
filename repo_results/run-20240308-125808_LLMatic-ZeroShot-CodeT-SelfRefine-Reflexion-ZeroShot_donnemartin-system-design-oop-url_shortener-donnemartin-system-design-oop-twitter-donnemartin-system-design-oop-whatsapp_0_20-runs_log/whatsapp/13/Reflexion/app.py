from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

users = {}

@dataclass
class User:
	email: str
	password: str

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	email = data['email']
	password = data['password']
	if email in users:
		return {'message': 'User already exists'}, 400
	user = User(email, password)
	users[email] = user
	return {'message': 'User created successfully'}, 201

if __name__ == '__main__':
	app.run(debug=True)
