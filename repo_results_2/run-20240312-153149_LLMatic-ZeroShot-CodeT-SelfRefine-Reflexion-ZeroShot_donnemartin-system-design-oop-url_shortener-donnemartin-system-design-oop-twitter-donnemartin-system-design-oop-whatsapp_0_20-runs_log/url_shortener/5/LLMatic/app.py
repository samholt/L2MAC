from flask import Flask, redirect, url_for, request, jsonify, session
from shortener import Shortener
from user import User
from admin import Admin

app = Flask(__name__)
app.secret_key = 'secret'
shortener = Shortener()
users = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	username = request.form['username']
	if username in users:
		return 'Username already exists', 400
	users[username] = User(username)
	session['username'] = username
	return 'User registered successfully'

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	if username not in users:
		return 'User not found', 404
	session['username'] = username
	return 'Logged in successfully'

@app.route('/<string:short_url>')
def redirect_to_url(short_url):
	url = shortener.get_original_url(short_url, request.remote_addr)
	if url is not None:
		return redirect(url)
	else:
		return 'Page not found', 404

@app.route('/analytics/<string:short_url>')
def get_analytics(short_url):
	analytics = shortener.get_analytics(short_url)
	return jsonify(analytics)

@app.route('/urls', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_urls():
	username = session.get('username')
	if username is None:
		return 'Not logged in', 401
	user = users[username]
	if request.method == 'GET':
		return jsonify(user.get_urls())
	elif request.method == 'POST':
		original_url = request.form['original_url']
		short_url = shortener.generate_short_url(original_url)
		user.create_url(original_url, short_url)
		return short_url
	elif request.method == 'PUT':
		short_url = request.form['short_url']
		new_url = request.form['new_url']
		user.edit_url(short_url, new_url)
		return 'URL updated'
	elif request.method == 'DELETE':
		short_url = request.form['short_url']
		user.delete_url(short_url)
		return 'URL deleted'

@app.route('/admin', methods=['GET', 'DELETE'])
def handle_admin():
	username = session.get('username')
	if username is None or not isinstance(users[username], Admin):
		return 'Not authorized', 403
	admin = users[username]
	if request.method == 'GET':
		return jsonify(admin.monitor_system())
	elif request.method == 'DELETE':
		target_username = request.form['target_username']
		if admin.delete_user(target_username):
			del users[target_username]
			return 'User deleted'
		else:
			return 'User not found', 404

@app.errorhandler(404)
def page_not_found(e):
	return 'Page not found', 404

@app.errorhandler(500)
def internal_server_error(e):
	return 'Internal server error. Please try again later.', 500

if __name__ == '__main__':
	app.run(debug=True)
