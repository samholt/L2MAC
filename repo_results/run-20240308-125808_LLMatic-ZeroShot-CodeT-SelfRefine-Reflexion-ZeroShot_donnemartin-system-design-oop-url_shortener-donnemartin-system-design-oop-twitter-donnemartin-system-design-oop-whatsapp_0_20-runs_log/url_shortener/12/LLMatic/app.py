from flask import Flask, redirect, abort, request
from url_shortener import generate_short_url, validate_url, get_original_url
from user_accounts import UserAccount
from analytics import track_click, get_analytics

app = Flask(__name__)
user_account = UserAccount()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_original_url(short_url):
	original_url = get_original_url(short_url)
	if original_url is None:
		abort(404)
	track_click(short_url, request.remote_addr)
	return redirect(original_url, code=302)

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = data['url']
	expiration_minutes = data.get('expiration_minutes', 10)
	if not validate_url(url):
		return 'Invalid URL.'
	short_url = generate_short_url(url, expiration_minutes)
	user_account.add_url(data['username'], short_url)
	return short_url

@app.route('/analytics/<short_url>')
def analytics(short_url):
	return str(get_analytics(short_url))

@app.route('/admin/dashboard')
def admin_dashboard():
	return str(user_account.accounts)

@app.route('/admin/delete_url', methods=['POST'])
def delete_url():
	data = request.get_json()
	username = data['username']
	url = data['url']
	return user_account.delete_url(username, url)

@app.route('/admin/delete_user', methods=['POST'])
def delete_user():
	data = request.get_json()
	username = data['username']
	if username in user_account.accounts:
		del user_account.accounts[username]
		return 'User deleted successfully.'
	return 'User does not exist.'

if __name__ == '__main__':
	app.run(debug=True)
