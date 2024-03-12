from flask import Flask, redirect, url_for, request
from url_shortener import DATABASE, validate_url, generate_short_url, custom_short_link, set_expiration
from analytics import track_click, get_analytics
from user_accounts import UserAccounts
from admin_dashboard import view_all_urls, delete_url, delete_user, monitor_system

app = Flask(__name__)
user_accounts = UserAccounts()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_url(short_url):
	for url, short in DATABASE.items():
		if short == short_url:
			track_click(short_url, request.remote_addr)
			return redirect(url)
	return 'URL not found', 404

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.form.get('url')
	custom_link = request.form.get('custom_link')
	expiration_time = request.form.get('expiration_time')
	if validate_url(url):
		if custom_link:
			short_url = custom_short_link(url, custom_link)
		else:
			short_url = generate_short_url(url)
		if expiration_time:
			set_expiration(short_url, int(expiration_time))
		return short_url
	else:
		return 'Invalid URL', 400

@app.route('/analytics/<short_url>')
def analytics(short_url):
	return str(get_analytics(short_url))

@app.route('/user/create', methods=['POST'])
def create_user():
	username = request.form.get('username')
	password = request.form.get('password')
	return user_accounts.create_account(username, password)

@app.route('/user/add_url', methods=['POST'])
def add_url():
	username = request.form.get('username')
	password = request.form.get('password')
	url = request.form.get('url')
	return user_accounts.add_url(username, password, url)

@app.route('/user/view_urls', methods=['POST'])
def view_urls():
	username = request.form.get('username')
	password = request.form.get('password')
	return str(user_accounts.view_urls(username, password))

@app.route('/user/delete_url', methods=['POST'])
def user_delete_url():
	username = request.form.get('username')
	password = request.form.get('password')
	url = request.form.get('url')
	return user_accounts.delete_url(username, password, url)

@app.route('/admin/view_all_urls')
def admin_view_all_urls():
	return str(view_all_urls())

@app.route('/admin/delete_url', methods=['POST'])
def admin_delete_url():
	url = request.form.get('url')
	return delete_url(url)

@app.route('/admin/delete_user', methods=['POST'])
def admin_delete_user():
	username = request.form.get('username')
	return delete_user(username)

@app.route('/admin/monitor_system')
def admin_monitor_system():
	return str(monitor_system())

if __name__ == '__main__':
	app.run(debug=True)
