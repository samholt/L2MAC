from flask import Flask, request, render_template
from user import User
from mock_db import MockDB
from contact import Contact
from message import Message
from group_chat import GroupChat

app = Flask(__name__)
db = MockDB()

@app.route('/')
def home():
	return render_template('home.html'), 200

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['password'])
	contact = Contact(data['email'])
	db.add(user.email, user)
	db.add(contact.email, contact)
	return render_template('register.html', message='User registered successfully'), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = db.retrieve(data['email'])
	if user and user.password == data['password']:
		user.set_online_status(True)
		return render_template('login.html', message='Login successful'), 200
	else:
		return render_template('login.html', message='Invalid email or password'), 401

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	user = db.retrieve(data['email'])
	if user and user.password == data['password']:
		user.set_online_status(False)
		return 'Logout successful', 200
	else:
		return 'Invalid email or password', 401

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	sender = db.retrieve(data['sender'])
	receiver = db.retrieve(data['receiver'])
	if sender and receiver and sender.password == data['password']:
		message = Message(sender.email, receiver.email, data['content'])
		if receiver.get_online_status():
			receiver.receive_message(message.send_message())
		else:
			receiver.add_to_message_queue(message.send_message())
		return 'Message sent', 200
	else:
		return 'Invalid email or password', 401

@app.route('/status', methods=['GET'])
def status():
	data = request.get_json()
	user = db.retrieve(data['email'])
	if user:
		return render_template('status.html', status=user.get_online_status()), 200
	else:
		return 'User not found', 404

if __name__ == '__main__':
	app.run(debug=True)
