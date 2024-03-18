from flask import Flask, redirect, abort, request
from shortener import Shortener
import datetime
from models import User, URL

app = Flask(__name__)
app.shortener = Shortener()
app.users = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	username = request.form.get('username')
	password = request.form.get('password')
	if username in app.users:
		abort(400)
	app.users[username] = User(username, password)
	return 'User registered successfully', 201

@app.route('/login', methods=['POST'])
def login():
	username = request.form.get('username')
	password = request.form.get('password')
	user = app.users.get(username)
	if user is None or user.password != password:
		abort(401)
	return 'User logged in successfully'

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = app.shortener.urls.get(short_url)
	if url is not None:
		if url.expiration_date and url.expiration_date < datetime.datetime.now():
			abort(410, 'URL has expired')
		url.clicks += 1
		click_detail = {'time': str(datetime.datetime.now()), 'ip': request.remote_addr}
		url.click_details.append(click_detail)
		return redirect(url.original_url, code=302)
	else:
		abort(404)

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	username = request.args.get('username')
	user = app.users.get(username)
	if user is None or not user.isAdmin:
		abort(403)
	return {'users': app.users, 'urls': app.shortener.urls}

@app.route('/admin/delete_user', methods=['DELETE'])
def delete_user():
	username = request.args.get('username')
	admin_username = request.args.get('admin_username')
	admin_user = app.users.get(admin_username)
	if admin_user is None or not admin_user.isAdmin:
		abort(403)
	if username in app.users:
		del app.users[username]
	return 'User deleted successfully'

@app.route('/admin/delete_url', methods=['DELETE'])
def delete_url():
	short_url = request.args.get('short_url')
	admin_username = request.args.get('admin_username')
	admin_user = app.users.get(admin_username)
	if admin_user is None or not admin_user.isAdmin:
		abort(403)
	if short_url in app.shortener.urls:
		del app.shortener.urls[short_url]
	return 'URL deleted successfully'

if __name__ == '__main__':
	app.run(debug=True)
