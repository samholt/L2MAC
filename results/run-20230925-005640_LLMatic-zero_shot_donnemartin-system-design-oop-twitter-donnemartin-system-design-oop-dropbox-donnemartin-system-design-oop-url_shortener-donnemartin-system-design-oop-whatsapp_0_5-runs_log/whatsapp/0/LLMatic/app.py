from flask import Flask, request
from user import User
from contact import Contact
from message import Message
from group import Group
from status import Status
from database import Database

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user = User(data['email'], data['password'])
	Database.add_user(user)
	return 'User created successfully'

@app.route('/recover_password', methods=['POST'])
def recover_password():
	data = request.get_json()
	user = Database.users.get(data['email'])
	if user:
		return user.recover_password(data['email'])
	else:
		return 'User not found'

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	data = request.get_json()
	user = Database.users.get(data['email'])
	if user:
		user.set_profile_picture(data['picture'])
		return 'Profile picture updated'
	else:
		return 'User not found'

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	data = request.get_json()
	user = Database.users.get(data['email'])
	if user:
		user.set_status_message(data['message'])
		return 'Status message updated'
	else:
		return 'User not found'

@app.route('/set_privacy_settings', methods=['POST'])
def set_privacy_settings():
	data = request.get_json()
	user = Database.users.get(data['email'])
	if user:
		user.set_privacy_settings(data['settings'])
		return 'Privacy settings updated'
	else:
		return 'User not found'

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	user = Database.users.get(data['email'])
	contact = Database.users.get(data['contact_email'])
	if user and contact:
		contact_obj = Contact(user, contact)
		contact_obj.block()
		return 'Contact blocked'
	else:
		return 'User or contact not found'

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	user = Database.users.get(data['email'])
	contact = Database.users.get(data['contact_email'])
	if user and contact:
		contact_obj = Contact(user, contact)
		contact_obj.unblock()
		return 'Contact unblocked'
	else:
		return 'User or contact not found'

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	sender = Database.users.get(data['sender_email'])
	receiver = Database.users.get(data['receiver_email'])
	if sender and receiver:
		message = Message(sender, receiver, data['content'])
		message.send(Database)
		Database.add_message(message)
		return 'Message sent'
	else:
		return 'Sender or receiver not found'

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	group = Group(data['name'], data['picture'])
	Database.add_group(group)
	return 'Group created'

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	user = Database.users.get(data['email'])
	if user:
		status = Status(user, data['content'], data['visibility'])
		Database.add_status(status)
		return 'Status posted'
	else:
		return 'User not found'

if __name__ == '__main__':
	app.run(debug=True)
