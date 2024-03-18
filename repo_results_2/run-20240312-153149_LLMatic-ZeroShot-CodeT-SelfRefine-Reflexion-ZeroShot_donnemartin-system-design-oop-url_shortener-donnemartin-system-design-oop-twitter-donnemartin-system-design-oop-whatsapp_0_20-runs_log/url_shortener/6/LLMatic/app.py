from flask import Flask, redirect, abort, request
from url_shortener import generate_short_url, validate_url, set_url_expiration, check_url_expiration
from analytics import record_click, get_analytics
from user_accounts import UserAccounts
from admin_dashboard import AdminDashboard

app = Flask(__name__)

# In-memory database for storing the mapping between original URLs and their shortened versions
url_db = {}

# User accounts and admin dashboard
user_accounts = UserAccounts()
admin_dashboard = AdminDashboard()

@app.route('/')
def home():
	# Home route, returns a simple greeting
	return 'Hello, World!'

@app.route('/shorten', methods=['POST'])
def shorten_url():
	# Route for shortening URLs
	# Takes a URL from the request JSON and returns a shortened version
	url = request.json.get('url')
	if validate_url(url):
		short_url = generate_short_url()
		url_db[short_url] = url
		return {'short_url': short_url}
	else:
		abort(400, 'Invalid URL')

@app.route('/<short_url>')
def redirect_to_original(short_url):
	# Route for redirecting from the shortened URL to the original URL
	# If the URL is not found or has expired, returns an error
	original_url = url_db.get(short_url)
	if original_url:
		if check_url_expiration(short_url):
			abort(410, 'URL has expired')
		record_click(short_url)
		return redirect(original_url)
	else:
		abort(404)

@app.route('/analytics/<short_url>')
def view_analytics(short_url):
	# Route for viewing analytics for a specific shortened URL
	return {'analytics': get_analytics(short_url)}

@app.route('/user/create', methods=['POST'])
def create_user():
	# Route for creating a new user account
	# Takes a username and password from the request JSON
	username = request.json.get('username')
	password = request.json.get('password')
	if user_accounts.create_account(username, password):
		return {'message': 'Account created successfully'}
	else:
		abort(400, 'Username already exists')

@app.route('/user/login', methods=['POST'])
def login_user():
	# Route for logging in a user
	# Takes a username and password from the request JSON
	username = request.json.get('username')
	password = request.json.get('password')
	if user_accounts.login(username, password):
		return {'message': 'Logged in successfully'}
	else:
		abort(400, 'Invalid username or password')

@app.route('/user/logout', methods=['POST'])
def logout_user():
	# Route for logging out a user
	# Takes a username from the request JSON
	username = request.json.get('username')
	if user_accounts.logout(username):
		return {'message': 'Logged out successfully'}
	else:
		abort(400, 'Invalid username')

@app.route('/admin/view_urls')
def view_all_urls():
	# Route for viewing all URLs in the system (admin only)
	return {'urls': admin_dashboard.view_all_urls()}

if __name__ == '__main__':
	app.run(debug=True)
