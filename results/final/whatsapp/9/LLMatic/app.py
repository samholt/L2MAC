from flask import Flask, request
from user import User
from contact import Contact
from group import Group
from message import Message
from status import Status

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['password'])
	return {'message': user.sign_up({})}, 200

@app.route('/recover_password', methods=['POST'])
def recover_password():
	data = request.get_json()
	user = User(data['email'], data['password'])
	return {'message': user.recover_password()}, 200

@app.route('/profile', methods=['POST'])
def profile():
	data = request.get_json()
	user = User(data['email'], data['password'])
	user.set_profile_picture(data['picture'])
	user.set_status_message(data['message'])
	user.set_privacy_settings(data['settings'])
	return {'message': 'Profile updated successfully'}, 200

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	contact = Contact(User(data['email'], data['password']))
	contact.block_contact(User(data['block_email'], data['block_password']))
	return {'message': 'Contact blocked successfully'}, 200

@app.route('/message', methods=['POST'])
def send_message():
	data = request.get_json()
	message = Message(User(data['sender'], data['password']), User(data['receiver'], data['password']), data['content'])
	return {'message': message.send_text(data['text'])}, 200

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	group = Group(data['name'], data['picture'], data['participants'], data['admins'], data['messages'])
	return {'message': 'Group created successfully'}, 200

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	status = Status(User(data['email'], data['password']), data['image'], data['visibility'], data['expiry_time'])
	status.post_status()
	return {'message': 'Status posted successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
