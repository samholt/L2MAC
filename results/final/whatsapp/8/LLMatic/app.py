from flask import Flask, request
from user import User
from contact import Contact
from message import Message
from group_chat import GroupChat
from status import Status

app = Flask(__name__)

# Mock database
users_db = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['password'])
	user.sign_up(users_db)
	return {'message': 'User registered successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and user.password == data['password']:
		user.set_online_status(True)
		return {'message': 'User logged in successfully'}, 200
	return {'message': 'Invalid credentials'}, 401

@app.route('/profile', methods=['PUT'])
def update_profile():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user:
		user.set_profile_picture(data['picture'])
		user.set_status_message(data['status_message'])
		user.set_privacy_settings(data['privacy_settings'])
		return {'message': 'Profile updated successfully'}, 200
	return {'message': 'User not found'}, 404

@app.route('/contact', methods=['POST'])
def manage_contact():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user:
		contact = Contact(user)
		if data['action'] == 'block':
			contact.block_contact(data['contact_email'])
		elif data['action'] == 'unblock':
			contact.unblock_contact(data['contact_email'])
		return {'message': 'Contact managed successfully'}, 200
	return {'message': 'User not found'}, 404

@app.route('/message', methods=['POST'])
def send_message():
	data = request.get_json()
	sender = users_db.get(data['email'])
	if sender:
		receiver = users_db.get(data['receiver_email'])
		if receiver:
			message = Message(sender, receiver, data['content'])
			message.send_offline()
			return {'message': 'Message sent successfully'}, 200
		return {'message': 'Receiver not found'}, 404
	return {'message': 'Sender not found'}, 404

@app.route('/group', methods=['POST'])
def manage_group():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user:
		group_chat = GroupChat(data['name'], data['picture'], [user], {user: 'admin'})
		if data['action'] == 'add':
			group_chat.add_participant(users_db.get(data['participant_email']))
		elif data['action'] == 'remove':
			group_chat.remove_participant(users_db.get(data['participant_email']))
		return {'message': 'Group managed successfully'}, 200
	return {'message': 'User not found'}, 404

@app.route('/status', methods=['POST'])
def post_status():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user:
		status = Status(user, data['image'], data['visibility'])
		status.post()
		return {'message': 'Status posted successfully'}, 200
	return {'message': 'User not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
