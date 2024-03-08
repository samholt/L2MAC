from flask import Flask, request
from models import User

app = Flask(__name__)

# Mock database
clubs = {}
users = {}
roles = {'member': [], 'admin': ['create_meeting', 'delete_comment']}

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user_id = data['user_id']
	username = data['username']
	email = data['email']
	password = data['password']
	users[user_id] = User(username, email, password)
	return {'message': 'User created successfully'}, 200

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club_name = data['club_name']
	user_id = data['user_id']
	if club_name in clubs:
		return {'message': 'Club already exists'}, 400
	clubs[club_name] = {'members': [user_id], 'privacy': 'public'}
	users[user_id].roles.append('admin')
	return {'message': 'Club created successfully'}, 200

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club_name = data['club_name']
	user_id = data['user_id']
	if club_name not in clubs:
		return {'message': 'Club does not exist'}, 400
	if user_id in clubs[club_name]['members']:
		return {'message': 'User already in club'}, 400
	clubs[club_name]['members'].append(user_id)
	users[user_id].roles.append('member')
	return {'message': 'Joined club successfully'}, 200

@app.route('/set_privacy', methods=['POST'])
def set_privacy():
	data = request.get_json()
	club_name = data['club_name']
	privacy = data['privacy']
	if club_name not in clubs:
		return {'message': 'Club does not exist'}, 400
	clubs[club_name]['privacy'] = privacy
	return {'message': 'Privacy set successfully'}, 200

@app.route('/manage_roles', methods=['POST'])
def manage_roles():
	data = request.get_json()
	user_id = data['user_id']
	role = data['role']
	if user_id not in users:
		return {'message': 'User does not exist'}, 400
	users[user_id].roles.append(role)
	return {'message': 'Role added successfully'}, 200

if __name__ == '__main__':
	app.run()
