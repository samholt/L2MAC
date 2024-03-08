from flask import Flask, redirect, abort, request
from shortener import Shortener
from user import User
from admin import Admin

app = Flask(__name__)
shortener = Shortener()
users = {}
admins = {}

@app.route('/')
def home():
	# Home route
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_original(short_url):
	# Redirect to the original URL of a shortened URL
	original_url = shortener.get_original_url(short_url)
	if original_url is None:
		abort(404)
	return redirect(original_url, code=302)

@app.route('/shorten', methods=['POST'])
def shorten_url():
	# Shorten a URL
	url = request.form.get('url')
	if not shortener.validate_url(url):
		abort(400)
	short_url = shortener.shorten_url(url)
	return {'short_url': short_url}

@app.route('/user/create', methods=['POST'])
def create_user():
	# Create a user
	username = request.form.get('username')
	password = request.form.get('password')
	user = User(username, password, shortener)
	users[username] = user
	return {'message': 'User created successfully'}

@app.route('/user/<username>/urls', methods=['GET'])
def view_user_urls(username):
	# View a user's URLs
	user = users.get(username)
	if user is None:
		abort(404)
	return user.view_urls()

@app.route('/user/<username>/analytics', methods=['GET'])
def view_user_analytics(username):
	# View a user's analytics
	user = users.get(username)
	if user is None:
		abort(404)
	return user.view_analytics()

@app.route('/user/<username>/set-expiration', methods=['POST'])
def set_url_expiration(username):
	# Set a URL's expiration date
	user = users.get(username)
	if user is None:
		abort(404)
	short_url = request.form.get('short_url')
	expiration_date = request.form.get('expiration_date')
	try:
		user.set_expiration(short_url, expiration_date)
	except ValueError:
		abort(400)
	return {'message': 'Expiration date set successfully'}

@app.route('/admin/create', methods=['POST'])
def create_admin():
	# Create an admin
	username = request.form.get('username')
	password = request.form.get('password')
	admin = Admin(username, password, shortener, users)
	admins[username] = admin
	return {'message': 'Admin created successfully'}

@app.route('/admin/<username>/urls', methods=['GET'])
def view_admin_urls(username):
	# View all URLs as an admin
	admin = admins.get(username)
	if admin is None:
		abort(404)
	return admin.view_all_urls()

@app.route('/admin/<username>/delete-user', methods=['POST'])
def delete_user(username):
	# Delete a user as an admin
	admin = admins.get(username)
	if admin is None:
		abort(404)
	user_to_delete = request.form.get('user')
	admin.delete_user(user_to_delete)
	return {'message': 'User deleted successfully'}

if __name__ == '__main__':
	app.run(debug=True)
