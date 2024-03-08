from flask import Flask, render_template, request
from services import auth, contact, message, group, status

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		user = auth.login(email, password)
		if user:
			return render_template('dashboard.html', user=user)
	return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		user = auth.register(email, password)
		if user:
			return render_template('dashboard.html', user=user)
	return render_template('register.html')

@app.route('/contacts')
def contacts():
	user = auth.get_current_user()
	contacts = contact.get_contacts(user)
	return render_template('contacts.html', contacts=contacts)

@app.route('/messages')
def messages():
	user = auth.get_current_user()
	messages = message.get_messages(user)
	return render_template('messages.html', messages=messages)

@app.route('/groups')
def groups():
	user = auth.get_current_user()
	groups = group.get_groups(user)
	return render_template('groups.html', groups=groups)

@app.route('/status')
def status_view():
	user = auth.get_current_user()
	statuses = status.get_statuses(user)
	return render_template('status.html', statuses=statuses)

if __name__ == '__main__':
	app.run(debug=True)
