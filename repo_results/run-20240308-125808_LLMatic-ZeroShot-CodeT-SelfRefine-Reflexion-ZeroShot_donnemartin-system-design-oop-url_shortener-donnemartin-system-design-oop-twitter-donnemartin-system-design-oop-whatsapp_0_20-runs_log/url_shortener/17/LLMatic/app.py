from flask import Flask, redirect, abort, request
from datetime import datetime
from url_shortener import generate_short_url, validate_url
from analytics import track_click, get_click_data
from user_accounts import UserAccounts
from admin_dashboard import AdminDashboard

app = Flask(__name__)

# Mock databases
url_db = {}
analytics_db = {}
user_accounts = UserAccounts()
admin_dashboard = AdminDashboard(url_db, user_accounts)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_url(short_url):
	if short_url in url_db:
		url_data = url_db[short_url]
		if url_data['expiration_datetime'] and datetime.now() > url_data['expiration_datetime']:
			abort(404)
		track_click(short_url, request.remote_addr)
		return redirect(url_data['url'])
	else:
		abort(404)

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.form.get('url')
	custom_short_url = request.form.get('custom_short_url')
	expiration_time = request.form.get('expiration_time')
	if validate_url(url):
		short_url, expiration_datetime = generate_short_url(url, custom_short_url, expiration_time)
		url_db[short_url] = {'url': url, 'expiration_datetime': expiration_datetime}
		return {'short_url': short_url}
	else:
		abort(400, 'Invalid URL')

@app.route('/analytics/<short_url>')
def analytics(short_url):
	return {'click_data': get_click_data(short_url)}

@app.route('/create_account', methods=['POST'])
def create_account():
	username = request.form.get('username')
	return {'message': user_accounts.create_account(username)}

@app.route('/add_url', methods=['POST'])
def add_url():
	username = request.form.get('username')
	url = request.form.get('url')
	return {'message': user_accounts.add_url(username, url)}

@app.route('/view_urls/<username>')
def view_urls(username):
	return {'urls': user_accounts.view_urls(username)}

@app.route('/delete_url', methods=['DELETE'])
def delete_url():
	username = request.form.get('username')
	url = request.form.get('url')
	return {'message': user_accounts.delete_url(username, url)}

@app.route('/edit_url', methods=['PUT'])
def edit_url():
	username = request.form.get('username')
	old_url = request.form.get('old_url')
	new_url = request.form.get('new_url')
	return {'message': user_accounts.edit_url(username, old_url, new_url)}

@app.route('/admin/view_all_urls')
def admin_view_all_urls():
	return {'all_urls': admin_dashboard.view_all_urls()}

@app.route('/admin/delete_url', methods=['DELETE'])
def admin_delete_url():
	short_url = request.form.get('short_url')
	return {'message': admin_dashboard.delete_url(short_url)}

@app.route('/admin/delete_user', methods=['DELETE'])
def admin_delete_user():
	username = request.form.get('username')
	return {'message': admin_dashboard.delete_user(username)}

@app.route('/admin/monitor_system')
def admin_monitor_system():
	return admin_dashboard.monitor_system()

if __name__ == '__main__':
	app.run(debug=True)
