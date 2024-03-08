from flask import Flask, render_template, request
from auth import Auth
from profile import Profile
from contacts import Contacts
from messaging import Messaging
from groups import Groups
from status import Status

app = Flask(__name__)

auth = Auth()


class WebApp:
	def __init__(self, username):
		self.app = app
		self.auth = auth
		self.profile = Profile(username)
		self.contacts = Contacts()
		self.messaging = Messaging()
		self.groups = Groups()
		self.status = Status(self.profile)

@app.route('/')

def home():
	return 'Welcome to the Chat App'

@app.route('/login', methods=['POST'])

def login():
	username = request.form['username']
	password = request.form['password']
	if auth.validate_user(username, password):
		return 'Login Successful'
	else:
		return 'Login Failed'

@app.route('/register', methods=['POST'])

def register():
	username = request.form['username']
	password = request.form['password']
	if auth.signup(username, password):
		return 'Registration Successful'
	else:
		return 'Registration Failed'

@app.route('/send_message', methods=['POST'])

def send_message():
	message = request.form['message']
	recipient = request.form['recipient']
	username = request.form['username']
	if Messaging().send_message(username, recipient, message):
		return 'Message Sent'
	else:
		return 'Message Failed'

@app.route('/create_group', methods=['POST'])

def create_group():
	group_name = request.form['group_name']
	username = request.form['username']
	if Groups().create_group(group_name, username):
		return 'Group Created'
	else:
		return 'Group Creation Failed'

@app.route('/update_status', methods=['POST'])

def update_status():
	new_status = request.form['new_status']
	username = request.form['username']
	if Status(Profile(username)).post_status(new_status):
		return 'Status Updated'
	else:
		return 'Status Update Failed'

if __name__ == '__main__':
	app.run(debug=True)
