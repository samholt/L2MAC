from flask import Flask, request

app = Flask(__name__)

# Mock database
users_db = {}
groups_db = {}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	if data['email'] in users_db:
		return {'message': 'User already exists'}, 400
	users_db[data['email']] = data
	return {'message': 'User created'}, 201

@app.route('/user/<email>', methods=['GET'])
def get_user(email):
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	return user, 200

@app.route('/user/<email>/reset_password', methods=['POST'])
def reset_password(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['password'] = data['new_password']
	return {'message': 'Password reset successful'}, 200

@app.route('/user/<email>/profile_picture', methods=['POST'])
def set_profile_picture(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['profile_picture'] = data['profile_picture']
	return {'message': 'Profile picture set'}, 200

@app.route('/user/<email>/status_message', methods=['POST'])
def set_status_message(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['status_message'] = data['status_message']
	return {'message': 'Status message set'}, 200

@app.route('/user/<email>/privacy_settings', methods=['POST'])
def update_privacy_settings(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['privacy_settings'] = data['privacy_settings']
	return {'message': 'Privacy settings updated'}, 200

@app.route('/user/<email>/block', methods=['POST'])
def block_contact(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['blocked_contacts'].append(data['contact_email'])
	return {'message': 'Contact blocked'}, 200

@app.route('/user/<email>/unblock', methods=['POST'])
def unblock_contact(email):
	data = request.get_json()
	user = users_db.get(email)
	if not user:
		return {'message': 'User not found'}, 404
	user['blocked_contacts'].remove(data['contact_email'])
	return {'message': 'Contact unblocked'}, 200

@app.route('/group', methods=['POST'])
def create_group():
	data = request.get_json()
	group_id = len(groups_db) + 1
	groups_db[group_id] = {'name': data['name'], 'members': data['members']}
	return {'message': 'Group created', 'group_id': group_id}, 201

@app.route('/group/<int:group_id>', methods=['GET'])
def get_group(group_id):
	group = groups_db.get(group_id)
	if not group:
		return {'message': 'Group not found'}, 404
	return group, 200

@app.route('/group/<int:group_id>/edit', methods=['POST'])
def edit_group(group_id):
	data = request.get_json()
	group = groups_db.get(group_id)
	if not group:
		return {'message': 'Group not found'}, 404
	group['name'] = data.get('name', group['name'])
	group['members'] = data.get('members', group['members'])
	return {'message': 'Group updated'}, 200

if __name__ == '__main__':
	app.run(debug=True)
