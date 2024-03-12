from flask import Flask, redirect, url_for, request
from shortener import Shortener
from user import User
from admin import Admin

app = Flask(__name__)
shortener = Shortener()
users = {}
admins = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_original(short_url):
	original_url = shortener.get_original_url(short_url)
	if original_url is not None:
		return redirect(original_url)
	else:
		return 'URL not found', 404

@app.route('/shorten', methods=['POST'])
def shorten_url():
	original_url = request.form['url']
	if shortener.validate_url(original_url):
		short_url = shortener.generate_short_url(original_url)
		return short_url
	else:
		return 'Invalid URL', 400

@app.route('/user/create', methods=['POST'])
def create_user():
	username = request.form['username']
	password = request.form['password']
	if username not in users:
		user = User(username, password)
		users[username] = user
		return 'User created'
	else:
		return 'User already exists', 400

@app.route('/user/<username>/urls')
def view_user_urls(username):
	user = users.get(username)
	if user is not None:
		return user.view_urls()
	else:
		return 'User not found', 404

@app.route('/admin/create', methods=['POST'])
def create_admin():
	username = request.form['username']
	password = request.form['password']
	if username not in admins:
		admin = Admin(username, password)
		admins[username] = admin
		return 'Admin created'
	else:
		return 'Admin already exists', 400

@app.route('/admin/<username>/monitor')
def monitor_system(username):
	admin = admins.get(username)
	if admin is not None:
		admin.monitor_system()
		return 'Monitoring system'
	else:
		return 'Admin not found', 404

@app.errorhandler(404)
def page_not_found(e):
	return 'Page not found', 404

@app.errorhandler(500)
def internal_server_error(e):
	return 'Internal server error', 500

if __name__ == '__main__':
	app.run(debug=True)
