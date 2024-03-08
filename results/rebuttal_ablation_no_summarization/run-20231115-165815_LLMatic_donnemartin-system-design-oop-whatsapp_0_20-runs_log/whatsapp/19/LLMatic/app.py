from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
	return jsonify(users)

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user_id = str(uuid.uuid4())
	users[user_id] = data
	return jsonify({'user_id': user_id}), 201

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	user_id = data.get('user_id')
	if user_id in users:
		return jsonify({'message': 'Password reset link has been sent to your email.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	data = request.get_json()
	user_id = data.get('user_id')
	new_picture = data.get('new_picture')
	if user_id in users:
		users[user_id]['profile_picture'] = new_picture
		return jsonify({'message': 'Profile picture updated.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	data = request.get_json()
	user_id = data.get('user_id')
	new_message = data.get('new_message')
	if user_id in users:
		users[user_id]['status_message'] = new_message
		return jsonify({'message': 'Status message updated.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

@app.route('/update_privacy_settings', methods=['POST'])
def update_privacy_settings():
	data = request.get_json()
	user_id = data.get('user_id')
	new_settings = data.get('new_settings')
	if user_id in users:
		users[user_id]['privacy_settings'] = new_settings
		return jsonify({'message': 'Privacy settings updated.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	user_id = data.get('user_id')
	contact_id = data.get('contact_id')
	if user_id in users:
		users[user_id]['blocked_contacts'].append(contact_id)
		return jsonify({'message': 'Contact blocked.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	user_id = data.get('user_id')
	contact_id = data.get('contact_id')
	if user_id in users and contact_id in users[user_id]['blocked_contacts']:
		users[user_id]['blocked_contacts'].remove(contact_id)
		return jsonify({'message': 'Contact unblocked.'}), 200
	else:
		return jsonify({'message': 'User not found or contact not blocked.'}), 404

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	user_id = data.get('user_id')
	group_details = data.get('group_details')
	if user_id in users:
		users[user_id]['groups'].append(group_details)
		return jsonify({'message': 'Group created.'}), 200
	else:
		return jsonify({'message': 'User not found.'}), 404

if __name__ == '__main__':
	app.run(debug=True)
