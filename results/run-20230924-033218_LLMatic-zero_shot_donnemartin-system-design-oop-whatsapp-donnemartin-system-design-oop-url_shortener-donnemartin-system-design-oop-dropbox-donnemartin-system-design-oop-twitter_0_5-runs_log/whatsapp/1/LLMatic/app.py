from flask import Flask, request
from user import User
from contact import Contact
from message import Message
from group import Group
from status import Status

app = Flask(__name__)
db = {}

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user = User(data['email'], data['password'])
	return user.sign_up(db)

@app.route('/signin', methods=['POST'])
def signin():
	data = request.get_json()
	user = db.get(data['email'])
	if user and user.password == data['password']:
		return 'User signed in successfully'
	return 'Invalid email or password'

@app.route('/recover_password', methods=['POST'])
def recover_password():
	data = request.get_json()
	user = User(data['email'], '')
	return user.recover_password(db)

@app.route('/view_profile', methods=['GET'])
def view_profile():
	data = request.get_json()
	user = db.get(data['email'])
	if user:
		return {'email': user.email, 'last_seen': user.last_seen, 'profile_picture': user.profile_picture, 'status_message': user.status_message, 'privacy_settings': user.privacy_settings}
	return 'User not found'

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	user = db.get(data['email'])
	if user:
		user.set_profile_picture(data['profile_picture'])
		user.set_status_message(data['status_message'])
		user.set_privacy_settings(data['privacy_settings'])
		return 'Profile updated successfully'
	return 'User not found'

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	user = db.get(data['email'])
	if user:
		contact = Contact(user)
		return contact.block_contact(db.get(data['contact_email']))
	return 'User not found'

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	user = db.get(data['email'])
	if user:
		contact = Contact(user)
		return contact.unblock_contact(db.get(data['contact_email']))
	return 'User not found'

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	user = db.get(data['email'])
	if user:
		contact = Contact(user)
		group = Group(data['group_name'], data['group_picture'], user)
		return contact.create_group(group)
	return 'User not found'

@app.route('/edit_group', methods=['POST'])
def edit_group():
	data = request.get_json()
	user = db.get(data['email'])
	if user:
		contact = Contact(user)
		group = Group(data['group_name'], data['group_picture'], user)
		new_group = Group(data['new_group_name'], data['new_group_picture'], user)
		return contact.edit_group(group, new_group)
	return 'User not found'

@app.route('/manage_group', methods=['POST'])
def manage_group():
	data = request.get_json()
	user = db.get(data['email'])
	if user:
		contact = Contact(user)
		group = Group(data['group_name'], data['group_picture'], user)
		return contact.manage_group(group)
	return 'User not found'

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	user = db.get(data['email'])
	if user:
		message = Message(user, db.get(data['receiver_email']), data['content'], data['read_receipt'], data['encryption'], data['attachments'])
		return {'message_id': message.send(db)}
	return 'User not found'

@app.route('/receive_message', methods=['GET'])
def receive_message():
	data = request.get_json()
	message = Message.receive(db, data['message_id'])
	if message:
		return {'sender': message.sender.email, 'receiver': message.receiver.email, 'content': message.content, 'read_receipt': message.read_receipt, 'encryption': message.encryption, 'attachments': message.attachments}
	return 'Message not found'

@app.route('/create_status', methods=['POST'])
def create_status():
	data = request.get_json()
	user = db.get(data['email'])
	if user:
		status = Status(user, data['content'], data['visibility'], data['duration'])
		status.post(db)
		return 'Status posted successfully'
	return 'User not found'

@app.route('/view_status', methods=['GET'])
def view_status():
	data = request.get_json()
	status = db.get(data['status_id'])
	if status:
		return {'user': status.user.email, 'content': status.content, 'visibility': status.visibility, 'expiry': status.expiry}
	return 'Status not found'

if __name__ == '__main__':
	app.run(debug=True)

