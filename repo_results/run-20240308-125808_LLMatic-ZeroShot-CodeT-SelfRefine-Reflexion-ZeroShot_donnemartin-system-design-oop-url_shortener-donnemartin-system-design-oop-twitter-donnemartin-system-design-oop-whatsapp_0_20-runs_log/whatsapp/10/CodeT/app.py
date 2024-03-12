from flask import Flask, request
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
users = {}
messages = {}

@dataclass
class User:
	id: str
	email: str
	password: str
	profile_picture: str
	status_message: str
	privacy_settings: dict
	blocked_contacts: list
	groups: list

@dataclass
class Message:
	id: str
	sender: str
	receiver: str
	content: str
	read: bool
	encrypted: bool

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return {'status': 'success'}, 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['id'])
	if user and user.password == data['password']:
		return {'status': 'success'}, 200
	return {'status': 'failure'}, 403

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	user = users.get(data['id'])
	if user and user.email == data['email']:
		user.password = data['new_password']
		return {'status': 'success'}, 200
	return {'status': 'failure'}, 403

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	user = users.get(data['id'])
	if user:
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.status_message = data.get('status_message', user.status_message)
		user.privacy_settings = data.get('privacy_settings', user.privacy_settings)
		return {'status': 'success'}, 200
	return {'status': 'failure'}, 403

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	user = users.get(data['id'])
	if user:
		user.blocked_contacts.append(data['contact_id'])
		return {'status': 'success'}, 200
	return {'status': 'failure'}, 403

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	user = users.get(data['id'])
	if user:
		user.blocked_contacts.remove(data['contact_id'])
		return {'status': 'success'}, 200
	return {'status': 'failure'}, 403

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	user = users.get(data['id'])
	if user:
		group = {'id': data['group_id'], 'name': data['name'], 'picture': data['picture'], 'participants': [user.id]}
		user.groups.append(group)
		return {'status': 'success'}, 200
	return {'status': 'failure'}, 403

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	message = Message(**data)
	messages[message.id] = message
	return {'status': 'success'}, 200

@app.route('/read_message', methods=['POST'])
def read_message():
	data = request.get_json()
	message = messages.get(data['id'])
	if message and message.receiver == data['user_id']:
		message.read = True
		return {'status': 'success'}, 200
	return {'status': 'failure'}, 403

if __name__ == '__main__':
	app.run(debug=True)
