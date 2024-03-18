from flask import Flask, redirect, abort, request
from url_shortener import url_database, is_expired, generate_short_url, validate_url
from user_accounts import users, User
from analytics import track_click, get_statistics

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_url(short_url):
	"""Redirect to the original URL.

	:param short_url: Shortened URL
	:return: Redirect to the original URL or 404 if the URL does not exist
	"""
	if short_url in url_database and not is_expired(short_url):
		track_click(short_url, request.remote_addr)
		return redirect(url_database[short_url]['url'])
	else:
		abort(404)

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	custom_short_url = request.json.get('custom_short_url')
	expiration_date = request.json.get('expiration_date')
	username = request.json.get('username')
	if validate_url(url):
		short_url = generate_short_url(url, custom_short_url, expiration_date)
		User.add_url(username, short_url, url)
		return {'short_url': short_url}
	else:
		abort(400)

@app.route('/analytics/<short_url>')
def view_analytics(short_url):
	return {'statistics': get_statistics(short_url)}

@app.route('/user/<username>')
def view_user_urls(username):
	return {'urls': User.view_urls(username)}

# Admin routes
@app.route('/admin/view_all_urls')
def admin_view_all_urls():
	return {'urls': User.view_all_urls()}

@app.route('/admin/delete_user/<username>', methods=['DELETE'])
def admin_delete_user(username):
	return {'success': User.delete_user(username)}

if __name__ == '__main__':
	app.run(debug=True)
