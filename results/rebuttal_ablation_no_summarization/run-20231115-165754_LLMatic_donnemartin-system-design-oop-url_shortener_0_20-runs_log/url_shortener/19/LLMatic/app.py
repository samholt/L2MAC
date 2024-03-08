from flask import Flask, redirect, abort, request
from url_shortener import generate_short_url, validate_url, store_url, get_url
from analytics import track_click, get_analytics
from user_accounts import UserAccount

app = Flask(__name__)

# Mock database
app.url_db = {}
app.user_db = {}
app.analytics_db = {}
app.user_accounts = UserAccount()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_url(short_url):
	original_url = get_url(app, short_url)
	if original_url:
		track_click(short_url, request.remote_addr)
		return redirect(original_url)
	else:
		abort(404)

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	original_url = request.form.get('url')
	expiration_minutes = int(request.form.get('expiration_minutes', 0))
	if validate_url(original_url):
		short_url = generate_short_url(original_url)
		store_url(app, short_url, original_url, expiration_minutes)
		return short_url
	else:
		abort(400)

@app.route('/analytics/<short_url>')
def analytics(short_url):
	return str(get_analytics(short_url))

@app.route('/create_account', methods=['POST'])
def create_account():
	username = request.form.get('username')
	return app.user_accounts.create_account(username)

@app.route('/view_urls/<username>')
def view_urls(username):
	return str(app.user_accounts.view_urls(username))

@app.route('/edit_url', methods=['POST'])
def edit_url():
	username = request.form.get('username')
	old_url = request.form.get('old_url')
	new_url = request.form.get('new_url')
	return app.user_accounts.edit_url(username, old_url, new_url)

@app.route('/delete_url', methods=['POST'])
def delete_url():
	username = request.form.get('username')
	url = request.form.get('url')
	return app.user_accounts.delete_url(username, url)

@app.route('/delete_user', methods=['POST'])
def delete_user():
	username = request.form.get('username')
	return app.user_accounts.delete_user(username)

if __name__ == '__main__':
	app.run(debug=True)
