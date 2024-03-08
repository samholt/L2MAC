from flask import Flask, redirect, url_for, request
from services.url_shortener import UrlShortener
from services.user_account import UserAccount
from services.admin_dashboard import AdminDashboard

app = Flask(__name__)
url_shortener = UrlShortener()
user_account = UserAccount()
admin_dashboard = AdminDashboard()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = url_shortener.get_original_url(short_url)
	if url is not None:
		url_shortener.record_click(short_url, 'mocked_location')
		return redirect(url)
	else:
		return 'URL not found', 404

@app.route('/analytics/<short_url>')
def get_analytics(short_url):
	analytics = url_shortener.get_analytics(short_url)
	if analytics is not None:
		return analytics
	else:
		return 'Analytics not found', 404

@app.route('/account/create', methods=['POST'])
def create_account():
	username = request.form.get('username')
	return user_account.create_account(username)

@app.route('/account/urls', methods=['GET'])
def view_urls():
	username = request.args.get('username')
	return user_account.view_urls(username)

@app.route('/account/edit_url', methods=['PUT'])
def edit_url():
	username = request.form.get('username')
	old_url = request.form.get('old_url')
	new_url = request.form.get('new_url')
	return user_account.edit_url(username, old_url, new_url)

@app.route('/account/delete_url', methods=['DELETE'])
def delete_url():
	username = request.form.get('username')
	url = request.form.get('url')
	return user_account.delete_url(username, url)

@app.route('/account/analytics', methods=['GET'])
def view_analytics():
	username = request.args.get('username')
	return user_account.view_analytics(username)

@app.route('/admin/urls', methods=['GET'])
def view_all_urls():
	return admin_dashboard.view_all_urls()

@app.route('/admin/delete_url', methods=['DELETE'])
def admin_delete_url():
	url = request.form.get('url')
	return admin_dashboard.delete_url(url)

@app.route('/admin/delete_user', methods=['DELETE'])
def delete_user():
	user = request.form.get('user')
	return admin_dashboard.delete_user(user)

@app.route('/admin/monitor', methods=['GET'])
def monitor_system():
	return admin_dashboard.monitor_system()

if __name__ == '__main__':
	app.run(debug=True)
