from flask import Flask, request
from models.user import User
from models.contact import Contact
from models.message import Message
from models.group import Group
from models.status import Status

app = Flask(__name__)

users = {}
contacts = {}
messages = {}
groups = {}
statuses = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return {'message': 'User registered successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['id'])
	if user and user.password == data['password']:
		return {'message': 'Login successful'}, 200
	return {'message': 'Invalid credentials'}, 401

if __name__ == '__main__':
	app.run(debug=True)
