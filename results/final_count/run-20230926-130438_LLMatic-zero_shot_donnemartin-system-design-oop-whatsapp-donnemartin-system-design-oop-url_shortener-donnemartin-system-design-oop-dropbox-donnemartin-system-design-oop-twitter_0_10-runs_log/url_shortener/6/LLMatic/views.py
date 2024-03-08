from flask import Flask, redirect, request, jsonify, session
from models import URL, ClickEvent, User
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super secret key'

# Mock database
DATABASE = {}
USERS = {'admin': User('admin', 'admin')}

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	if username in USERS:
		return 'Username already exists', 400
	user = User(username, password)
	USERS[username] = user
	return 'User registered successfully', 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if username not in USERS or USERS[username].password != password:
		return 'Invalid username or password', 400
	session['username'] = username
	return 'Logged in successfully', 200

@app.route('/logout', methods=['POST'])
def logout():
	session.pop('username', None)
	return 'Logged out successfully', 200

@app.route('/urls', methods=['GET'])
def get_urls():
	username = session.get('username')
	if not username:
		return 'Not logged in', 401
	user = USERS[username]
	urls = [{'original_url': url.original_url, 'shortened_url': url.shortened_url} for url in user.urls]
	return jsonify(urls)

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	if short_url in DATABASE:
		url = DATABASE[short_url]
		# Record a click event
		click_event = ClickEvent(datetime.now(), request.remote_addr)
		url.click_events.append(click_event)
		# Redirect to the original URL
		return redirect(url.original_url, code=302)
	else:
		return 'URL not found', 404

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	if short_url in DATABASE:
		url = DATABASE[short_url]
		clicks = len(url.click_events)
		click_events = [{'time': str(event.click_time), 'location': event.location} for event in url.click_events]
		return jsonify({'clicks': clicks, 'click_events': click_events})
	else:
		return 'URL not found', 404

@app.route('/admin/urls', methods=['GET'])
def admin_get_urls():
	# This is a mock check for admin user
	if session.get('username') != 'admin' or USERS[session.get('username')].password != 'admin':
		return 'Unauthorized', 401
	urls = [{'original_url': url.original_url, 'shortened_url': url.shortened_url} for url in DATABASE.values()]
	return jsonify(urls)

@app.route('/admin/users', methods=['GET'])
def admin_get_users():
	# This is a mock check for admin user
	if session.get('username') != 'admin' or USERS[session.get('username')].password != 'admin':
		return 'Unauthorized', 401
	users = [{'username': user.username} for user in USERS.values()]
	return jsonify(users)

@app.route('/admin/delete_url/<short_url>', methods=['DELETE'])
def admin_delete_url(short_url):
	# This is a mock check for admin user
	if session.get('username') != 'admin' or USERS[session.get('username')].password != 'admin':
		return 'Unauthorized', 401
	if short_url in DATABASE:
		del DATABASE[short_url]
		return 'URL deleted successfully', 200
	else:
		return 'URL not found', 404

@app.route('/admin/delete_user/<username>', methods=['DELETE'])
def admin_delete_user(username):
	# This is a mock check for admin user
	if session.get('username') != 'admin' or USERS[session.get('username')].password != 'admin':
		return 'Unauthorized', 401
	if username in USERS:
		del USERS[username]
		return 'User deleted successfully', 200
	else:
		return 'User not found', 404

@app.route('/set_expiration/<short_url>', methods=['POST'])
def set_expiration(short_url):
	# Check if the user is logged in
	username = session.get('username')
	if not username:
		return 'Not logged in', 401
	# Check if the URL exists
	if short_url not in DATABASE:
		return 'URL not found', 404
	url = DATABASE[short_url]
	# Check if the user is the owner of the URL
	if url.user.username != username:
		return 'Not authorized', 403
	# Set the expiration date
	expiration_date = request.json.get('expiration_date')
	url.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
	return 'Expiration date set successfully', 200

@app.route('/admin/stats', methods=['GET'])
def admin_get_stats():
	# This is a mock check for admin user
	if session.get('username') != 'admin' or USERS[session.get('username')].password != 'admin':
		return 'Unauthorized', 401
	total_urls = len(DATABASE)
	total_users = len(USERS)
	total_clicks = sum(len(url.click_events) for url in DATABASE.values())
	return jsonify({'total_urls': total_urls, 'total_users': total_users, 'total_clicks': total_clicks})

if __name__ == '__main__':
	app.run(debug=True)
