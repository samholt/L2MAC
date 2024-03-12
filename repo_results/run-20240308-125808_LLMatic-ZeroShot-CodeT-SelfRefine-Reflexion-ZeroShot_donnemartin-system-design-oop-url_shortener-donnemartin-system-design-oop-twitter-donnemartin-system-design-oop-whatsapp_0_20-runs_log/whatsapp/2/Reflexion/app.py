from flask import Flask, request
from database import users, groups
from models import User, Group

app = Flask(__name__)

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

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
	user = users.get(user_id)
	if user:
		return user.__dict__, 200
	return {'message': 'User not found'}, 404

@app.route('/group', methods=['POST'])
def create_group():
	data = request.get_json()
	group = Group(**data)
	groups[group.id] = group
	return {'message': 'Group created successfully'}, 201

@app.route('/group/<group_id>', methods=['GET'])
def get_group(group_id):
	group = groups.get(group_id)
	if group:
		return group.__dict__, 200
	return {'message': 'Group not found'}, 404
