from flask import Flask, redirect, abort, request
from url_shortener import set_expiration, generate_short_url, validate_url
from analytics import track_click, get_statistics
from user_accounts import UserAccounts
from datetime import datetime

app = Flask(__name__)

url_map = {}
url_expiration = {}
user_accounts = UserAccounts()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_url(short_url):
	if short_url in url_map:
		if datetime.now() > url_expiration[short_url]:
			abort(410)
		else:
			track_click(short_url, request.remote_addr)
			return redirect(url_map[short_url])
	else:
		abort(404)

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.form.get('url')
	custom_short_url = request.form.get('custom_short_url')
	username = request.form.get('username')
	if validate_url(url):
		short_url = custom_short_url if custom_short_url else generate_short_url(url)
		url_map[short_url] = url
		url_expiration[short_url] = set_expiration(short_url)
		if username:
			user_accounts.add_url(username, short_url)
		return short_url
	else:
		return 'Invalid URL'

@app.route('/statistics/<short_url>')
def view_statistics(short_url):
	return str(get_statistics(short_url))

@app.route('/admin/urls')
def view_all_urls():
	return str(url_map)

@app.route('/admin/delete_url', methods=['POST'])
def delete_url():
	url = request.form.get('url')
	if url in url_map:
		del url_map[url]
		del url_expiration[url]
		return 'URL deleted'
	else:
		return 'URL not found'

@app.route('/admin/delete_user', methods=['POST'])
def delete_user():
	username = request.form.get('username')
	if username in user_accounts.users:
		del user_accounts.users[username]
		return 'User deleted'
	else:
		return 'User not found'

if __name__ == '__main__':
	app.run(debug=True)
