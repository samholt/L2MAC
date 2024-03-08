from flask import Flask, request, jsonify
from dataclasses import dataclass
import json

app = Flask(__name__)

users = {}
sessions = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str
	status_message: str
	privacy_settings: dict
	contacts: list
	blocked_contacts: list
	groups: list
	messages: list
	status: list

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = users.get(email)
	if not user or user.password != password:
		return jsonify({'message': 'Invalid email or password'}), 401
	sessions[email] = 'Logged In'
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	email = data.get('email')
	sessions.pop(email, None)
	return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	email = data.get('email')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.password = 'new_password'
	return jsonify({'message': 'Password reset successfully'}), 200

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	data = request.get_json()
	email = data.get('email')
	profile_picture = data.get('profile_picture')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.profile_picture = profile_picture
	return jsonify({'message': 'Profile picture set successfully'}), 200

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	data = request.get_json()
	email = data.get('email')
	status_message = data.get('status_message')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.status_message = status_message
	return jsonify({'message': 'Status message set successfully'}), 200

@app.route('/set_privacy_settings', methods=['POST'])
def set_privacy_settings():
	data = request.get_json()
	email = data.get('email')
	privacy_settings = data.get('privacy_settings')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.privacy_settings = privacy_settings
	return jsonify({'message': 'Privacy settings set successfully'}), 200

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	email = data.get('email')
	contact_email = data.get('contact_email')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.blocked_contacts.append(contact_email)
	return jsonify({'message': 'Contact blocked successfully'}), 200

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	email = data.get('email')
	contact_email = data.get('contact_email')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.blocked_contacts.remove(contact_email)
	return jsonify({'message': 'Contact unblocked successfully'}), 200

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	email = data.get('email')
	group_name = data.get('group_name')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.groups.append(group_name)
	return jsonify({'message': 'Group created successfully'}), 200

@app.route('/edit_group', methods=['POST'])
def edit_group():
	data = request.get_json()
	email = data.get('email')
	old_group_name = data.get('old_group_name')
	new_group_name = data.get('new_group_name')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.groups.remove(old_group_name)
	user.groups.append(new_group_name)
	return jsonify({'message': 'Group edited successfully'}), 200

@app.route('/delete_group', methods=['POST'])
def delete_group():
	data = request.get_json()
	email = data.get('email')
	group_name = data.get('group_name')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.groups.remove(group_name)
	return jsonify({'message': 'Group deleted successfully'}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	email = data.get('email')
	message = data.get('message')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.messages.append(message)
	return jsonify({'message': 'Message sent successfully'}), 200

@app.route('/read_message', methods=['POST'])
def read_message():
	data = request.get_json()
	email = data.get('email')
	message_index = data.get('message_index')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	message = user.messages[message_index]
	return jsonify({'message': message}), 200

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	email = data.get('email')
	status = data.get('status')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.status.append(status)
	return jsonify({'message': 'Status posted successfully'}), 200

@app.route('/view_status', methods=['POST'])
def view_status():
	data = request.get_json()
	email = data.get('email')
	status_index = data.get('status_index')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	status = user.status[status_index]
	return jsonify({'status': status}), 200

if __name__ == '__main__':
	app.run(debug=True)
