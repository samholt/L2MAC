from flask import Flask, request, jsonify
from user import UserDatabase
from contact import Contact, Group as ContactGroup
from message import Message, ImageMessage, EmojiMessage
from group import Group

app = Flask(__name__)

user_db = UserDatabase()

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	response = user_db.sign_up(data['email'], data['password'])
	return jsonify({'message': response}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['email'] in user_db.users and user_db.users[data['email']].password == data['password']:
		return jsonify({'message': 'Login successful'}), 200
	else:
		return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	data = request.get_json()
	if request.method == 'POST':
		user = user_db.users[data['email']]
		user.set_profile_picture(data['profile_picture'])
		user.set_status_message(data['status_message'])
		user.set_privacy_setting(data['privacy_setting'])
		return jsonify({'message': 'Profile updated'}), 200
	else:
		user = user_db.users[data['email']]
		return jsonify({'email': user.email, 'profile_picture': user.profile_picture, 'status_message': user.status_message, 'privacy_setting': user.privacy_setting}), 200

@app.route('/contact', methods=['POST'])
def contact():
	data = request.get_json()
	contact = Contact(data['name'])
	return jsonify({'message': 'Contact created'}), 200

@app.route('/message', methods=['POST'])
def message():
	data = request.get_json()
	message = Message(data['sender'], data['receiver'], data['content'])
	message.send_message()
	return jsonify({'message': 'Message sent'}), 200

@app.route('/group', methods=['POST'])
def group():
	data = request.get_json()
	group = Group(data['group_name'], data['admin'])
	return jsonify({'message': 'Group created'}), 200

@app.route('/status', methods=['POST'])
def status():
	data = request.get_json()
	user = user_db.users[data['email']]
	user.post_status(data['content'], data['visibility_duration'], data['visibility_setting'])
	return jsonify({'message': 'Status posted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
