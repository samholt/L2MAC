from flask import Flask, request
from user import User
from contact import Contact
from message import Message
from group import Group
from status import Status

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['password'])
	user.register()
	return {'message': 'User registered successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User(data['email'], data['password'])
	user.login()
	return {'message': 'User logged in successfully'}, 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	user = User(data['email'], data['password'])
	user.logout()
	return {'message': 'User logged out successfully'}, 200

@app.route('/profile', methods=['GET', 'PUT'])
def profile():
	data = request.get_json()
	user = User(data['email'], data['password'])
	if request.method == 'GET':
		return {'profile_picture': user.profile_picture, 'status_message': user.status_message, 'privacy_settings': user.privacy_settings}, 200
	elif request.method == 'PUT':
		user.set_profile_picture(data['picture'])
		user.set_status_message(data['message'])
		user.set_privacy_settings(data['settings'])
		return {'message': 'Profile updated successfully'}, 200

@app.route('/block', methods=['POST'])
def block():
	data = request.get_json()
	contact = Contact(User(data['email'], data['password']))
	contact.block_contact(User(data['block_email'], data['block_password']))
	return {'message': 'Contact blocked successfully'}, 200

@app.route('/unblock', methods=['POST'])
def unblock():
	data = request.get_json()
	contact = Contact(User(data['email'], data['password']))
	contact.unblock_contact(User(data['unblock_email'], data['unblock_password']))
	return {'message': 'Contact unblocked successfully'}, 200

@app.route('/group', methods=['POST', 'PUT', 'DELETE'])
def group():
	data = request.get_json()
	contact = Contact(User(data['email'], data['password']))
	if request.method == 'POST':
		group = Group(data['name'], data['picture'], data['admins'])
		contact.create_group(group)
		return {'message': 'Group created successfully'}, 201
	elif request.method == 'PUT':
		group = Group(data['name'], data['picture'], data['admins'])
		new_group = Group(data['new_name'], data['new_picture'], data['new_admins'])
		contact.edit_group(group, new_group)
		return {'message': 'Group edited successfully'}, 200
	elif request.method == 'DELETE':
		group = Group(data['name'], data['picture'], data['admins'])
		contact.delete_group(group)
		return {'message': 'Group deleted successfully'}, 200

@app.route('/message', methods=['POST', 'PUT'])
def message():
	data = request.get_json()
	message = Message(User(data['sender_email'], data['sender_password']), User(data['receiver_email'], data['receiver_password']), data['content'])
	if request.method == 'POST':
		message.send()
		return {'message': 'Message sent successfully'}, 201
	elif request.method == 'PUT':
		message.read()
		return {'message': 'Message read successfully'}, 200

@app.route('/status', methods=['POST', 'GET', 'DELETE'])
def status():
	data = request.get_json()
	status = Status(User(data['email'], data['password']), data['content'], data['visibility'], data['expiry'])
	if request.method == 'POST':
		status.post()
		return {'message': 'Status posted successfully'}, 201
	elif request.method == 'GET':
		viewer = User(data['viewer_email'], data['viewer_password'])
		return {'status': status.view(viewer)}, 200
	elif request.method == 'DELETE':
		status.delete()
		return {'message': 'Status deleted successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
