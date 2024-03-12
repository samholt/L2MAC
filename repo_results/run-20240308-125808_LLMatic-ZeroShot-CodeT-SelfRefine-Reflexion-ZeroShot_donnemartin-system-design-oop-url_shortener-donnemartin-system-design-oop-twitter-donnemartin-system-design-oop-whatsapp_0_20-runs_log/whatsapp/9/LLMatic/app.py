from flask import Flask, request, render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)
app.secret_key = 'super secret key'

# Mock database
users = {}
contacts = {}
messages = []
groups = {}
statuses = {}


class User:
	def __init__(self, email, password):
		self.email = email
		self.password = generate_password_hash(password)
		self.contacts = []
		self.blocked_contacts = []
		self.profile_picture = None
		self.status_message = None
		self.is_online = False
		self.message_queue = []

	def check_password(self, password):
		return check_password_hash(self.password, password)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		data = request.form
		users[data['email']] = User(data['email'], data['password'])
		return redirect(url_for('login'))
	return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		data = request.form
		user = users.get(data['email'])
		if user and user.check_password(data['password']):
			session['email'] = data['email']
			return redirect(url_for('home'))
	return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('email', None)
	return redirect(url_for('login'))

@app.route('/')
def home():
	if 'email' in session:
		return f'Hello, {session["email"]}!'
	return redirect(url_for('login'))

@app.route('/connectivity', methods=['POST'])
def manage_connectivity():
	data = request.json
	user = users.get(data['email'])
	if user:
		user.is_online = data['is_online']
		if user.is_online and user.message_queue:
			for message in user.message_queue:
				messages.append(message)
			user.message_queue = []
	return '', 204

if __name__ == '__main__':
	app.run(debug=True)
