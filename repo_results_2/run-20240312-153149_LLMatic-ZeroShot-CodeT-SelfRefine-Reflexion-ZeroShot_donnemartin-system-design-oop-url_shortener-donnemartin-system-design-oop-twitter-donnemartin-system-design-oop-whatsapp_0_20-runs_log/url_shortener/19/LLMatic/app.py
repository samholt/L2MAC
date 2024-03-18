from flask import Flask, redirect, request
from url_shortener import URLShortener
from user_accounts import UserAccounts
from analytics import track_click, get_statistics

app = Flask(__name__)
url_shortener = URLShortener()
user_accounts = UserAccounts()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = url_shortener.get_original_url(short_url)
	if url is not None:
		track_click(short_url)
		return redirect(url)
	else:
		return 'URL not found', 404

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
	if request.method == 'POST':
		action = request.form.get('action')
		if action == 'view_urls':
			return str(url_shortener.get_all_urls())
		elif action == 'delete_url':
			short_url = request.form.get('short_url')
			url_shortener.delete_url(short_url)
			return 'URL deleted'
		elif action == 'delete_user':
			username = request.form.get('username')
			user_accounts.delete_user(username)
			return 'User deleted'
		elif action == 'view_statistics':
			short_url = request.form.get('short_url')
			return str(get_statistics(short_url))
	return 'Admin dashboard'

@app.route('/register', methods=['POST'])
def register():
	username = request.form.get('username')
	password = request.form.get('password')
	return user_accounts.register(username, password)

@app.route('/login', methods=['POST'])
def login():
	username = request.form.get('username')
	password = request.form.get('password')
	return user_accounts.login(username, password)

@app.route('/add_url', methods=['POST'])
def add_url():
	username = request.form.get('username')
	url = request.form.get('url')
	custom_short_link = request.form.get('custom_short_link')
	expiration_date = request.form.get('expiration_date')
	if url_shortener.validate_url(url):
		short_url = url_shortener.generate_short_url(url, custom_short_link, expiration_date)
		user_accounts.add_url(username, short_url)
		return 'Short URL: ' + short_url
	else:
		return 'Invalid URL'

if __name__ == '__main__':
	app.run(debug=True)
