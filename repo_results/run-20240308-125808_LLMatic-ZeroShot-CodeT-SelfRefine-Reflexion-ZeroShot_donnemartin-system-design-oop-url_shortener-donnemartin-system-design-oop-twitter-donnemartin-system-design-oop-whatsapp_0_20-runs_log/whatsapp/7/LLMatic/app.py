from flask import Flask, request
import random
import string
import time

app = Flask(__name__)

# Mock database
users_db = {}
groups_db = {}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	users_db[data['email']] = {'email': data['email'], 'password': data['password'], 'groups': [], 'statuses': [], 'last_activity': time.time(), 'offline_messages': []}
	return {'message': 'User created'}, 201

@app.route('/user/<email>', methods=['GET'])
def get_user(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['online'] = time.time() - user['last_activity'] < 300
	return user, 200

@app.route('/user/<email>/connectivity', methods=['POST'])
def update_connectivity(email):
	data = request.get_json()
	if 'online' not in data:
		return {'message': 'Online status is required'}, 400
	if email not in users_db:
		return {'message': 'User not found'}, 404
	users_db[email]['last_activity'] = time.time() if data['online'] else time.time() - 301
	if data['online'] and users_db[email]['offline_messages']:
		users_db[email]['statuses'].extend(users_db[email]['offline_messages'])
		users_db[email]['offline_messages'] = []
	return {'message': 'Connectivity updated'}, 200

@app.route('/status/post', methods=['POST'])
def post_status():
	data = request.get_json()
	if 'email' not in data or 'status' not in data:
		return {'message': 'Email and status are required'}, 400
	if data['email'] not in users_db:
		return {'message': 'User not found'}, 404
	status_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
	status = {'id': status_id, 'status': data['status'], 'visibility': 'public'}
	if time.time() - users_db[data['email']]['last_activity'] < 300:
		users_db[data['email']]['statuses'].append(status)
		return {'message': 'Status posted', 'status_id': status_id}, 201
	else:
		users_db[data['email']]['offline_messages'].append(status)
		return {'message': 'User is offline, status added to queue', 'status_id': status_id}, 201

@app.route('/status/<status_id>/visibility', methods=['POST'])
def control_visibility(status_id):
	data = request.get_json()
	if 'email' not in data or 'visibility' not in data:
		return {'message': 'Email and visibility are required'}, 400
	if data['email'] not in users_db:
		return {'message': 'User not found'}, 404
	for status in users_db[data['email']]['statuses']:
		if status['id'] == status_id:
			status['visibility'] = data['visibility']
			return {'message': 'Visibility updated'}, 200
	return {'message': 'Status not found'}, 404

@app.route('/group/create', methods=['POST'])
def create_group():
	data = request.get_json()
	if 'email' not in data or 'group_name' not in data:
		return {'message': 'Email and group name are required'}, 400
	if data['email'] not in users_db:
		return {'message': 'User not found'}, 404
	group_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
	groups_db[group_id] = {'name': data['group_name'], 'admin': data['email'], 'members': [data['email']], 'admin_roles': {data['email']: 'admin'}}
	users_db[data['email']]['groups'].append(group_id)
	return {'message': 'Group created', 'group_id': group_id}, 201

@app.route('/group/<group_id>/add', methods=['POST'])
def add_participant(group_id):
	data = request.get_json()
	if 'email' not in data or 'participant_email' not in data:
		return {'message': 'Email and participant email are required'}, 400
	if data['email'] not in users_db or data['participant_email'] not in users_db:
		return {'message': 'User or participant not found'}, 404
	if group_id not in groups_db or data['email'] not in groups_db[group_id]['members']:
		return {'message': 'Group not found or user not in group'}, 404
	groups_db[group_id]['members'].append(data['participant_email'])
	users_db[data['participant_email']]['groups'].append(group_id)
	return {'message': 'Participant added'}, 200

@app.route('/group/<group_id>/remove', methods=['POST'])
def remove_participant(group_id):
	data = request.get_json()
	if 'email' not in data or 'participant_email' not in data:
		return {'message': 'Email and participant email are required'}, 400
	if data['email'] not in users_db or data['participant_email'] not in users_db:
		return {'message': 'User or participant not found'}, 404
	if group_id not in groups_db or data['email'] not in groups_db[group_id]['members']:
		return {'message': 'Group not found or user not in group'}, 404
	if data['participant_email'] in groups_db[group_id]['members']:
		groups_db[group_id]['members'].remove(data['participant_email'])
	if group_id in users_db[data['participant_email']]['groups']:
		users_db[data['participant_email']]['groups'].remove(group_id)
	return {'message': 'Participant removed'}, 200

@app.route('/group/<group_id>/admin', methods=['POST'])
def manage_admin(group_id):
	data = request.get_json()
	if 'email' not in data or 'admin_email' not in data or 'role' not in data:
		return {'message': 'Email, admin email and role are required'}, 400
	if data['email'] not in users_db or data['admin_email'] not in users_db:
		return {'message': 'User or admin not found'}, 404
	if group_id not in groups_db or data['email'] != groups_db[group_id]['admin']:
		return {'message': 'Group not found or user not admin'}, 404
	groups_db[group_id]['admin_roles'][data['admin_email']] = data['role']
	return {'message': 'Admin roles updated'}, 200
