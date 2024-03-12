from flask import Flask, redirect, abort, request
from url_shortener import generate_short_url, validate_url, handle_custom_short_link, set_expiration, is_expired
from analytics import track_click, get_analytics
from user_accounts import UserAccount
from admin_dashboard import AdminDashboard

app = Flask(__name__)

url_database = {}
user_database = {}
admin = AdminDashboard(url_database, user_database)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.json['url']
	custom_link = request.json.get('custom_link')
	expiration_minutes = request.json.get('expiration_minutes')
	if validate_url(url):
		if custom_link:
			if handle_custom_short_link(custom_link, url_database):
				url_database[custom_link]['url'] = url
				if expiration_minutes:
					set_expiration(custom_link, url_database, expiration_minutes)
				return {'short_url': custom_link}
			else:
				return {'error': 'Custom link already in use'}, 400
		else:
			short_url = generate_short_url(url)
			url_database[short_url] = {'url': url, 'expiration': None}
			if expiration_minutes:
				set_expiration(short_url, url_database, expiration_minutes)
			return {'short_url': short_url}
	else:
		return {'error': 'Invalid URL'}, 400

@app.route('/<short_url>')
def redirect_to_url(short_url):
	if short_url in url_database:
		if is_expired(short_url, url_database):
			abort(410)
		else:
			track_click(short_url, request.remote_addr)
			return redirect(url_database[short_url]['url'])
	else:
		abort(404)

@app.route('/analytics/<short_url>')
def view_analytics(short_url):
	return {'analytics': get_analytics(short_url)}

@app.route('/user/<username>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_user(username):
	if request.method == 'POST':
		user_database[username] = UserAccount(username)
		return {'message': 'User created'}, 201
	elif request.method == 'GET':
		return {'urls': user_database[username].view_urls()}
	elif request.method == 'PUT':
		original_url = request.json['original_url']
		shortened_url = request.json['shortened_url']
		user_database[username].create_url(original_url, shortened_url)
		return {'message': 'URL added'}, 200
	elif request.method == 'DELETE':
		shortened_url = request.json['shortened_url']
		user_database[username].delete_url(shortened_url)
		return {'message': 'URL deleted'}, 200

@app.route('/admin', methods=['GET', 'DELETE'])
def admin_dashboard():
	if request.method == 'GET':
		return {'urls': admin.view_all_urls()}
	elif request.method == 'DELETE':
		short_url = request.json['short_url']
		admin.delete_url(short_url)
		return {'message': 'URL deleted'}, 200

if __name__ == '__main__':
	app.run(debug=True)
