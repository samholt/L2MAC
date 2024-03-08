from flask import Flask, redirect, request
from url_shortener import URLShortener
from analytics import Analytics
from user_accounts import UserAccounts
from admin_dashboard import AdminDashboard

app = Flask(__name__)
url_shortener = URLShortener()
analytics = Analytics()
user_accounts = UserAccounts()
admin_dashboard = AdminDashboard()

@app.route('/')
def home():
	return 'Hello, World!', 200

@app.route('/<short_url>')
def redirect_to_url(short_url):
	original_url = url_shortener.get_original_url(short_url)
	if original_url != 'URL not found':
		analytics.record(short_url)
		return redirect(original_url)
	else:
		return 'URL not found', 404

@app.route('/create_account', methods=['POST'])
def create_account():
	username = request.form.get('username')
	password = request.form.get('password')
	return user_accounts.create_account(username, password)

@app.route('/view_urls', methods=['POST'])
def view_urls():
	username = request.form.get('username')
	password = request.form.get('password')
	return user_accounts.view_urls(username, password)

@app.route('/edit_url', methods=['POST'])
def edit_url():
	username = request.form.get('username')
	password = request.form.get('password')
	old_url = request.form.get('old_url')
	new_url = request.form.get('new_url')
	return user_accounts.edit_url(username, password, old_url, new_url)

@app.route('/delete_url', methods=['POST'])
def delete_url():
	username = request.form.get('username')
	password = request.form.get('password')
	url = request.form.get('url')
	return user_accounts.delete_url(username, password, url)

@app.route('/view_analytics', methods=['POST'])
def view_analytics():
	username = request.form.get('username')
	password = request.form.get('password')
	return user_accounts.view_analytics(username, password)

@app.route('/admin/view_all_urls')
def admin_view_all_urls():
	return admin_dashboard.view_all_urls()

@app.route('/admin/delete_url', methods=['POST'])
def admin_delete_url():
	url = request.form.get('url')
	return admin_dashboard.delete_url(url)

@app.route('/admin/delete_user', methods=['POST'])
def admin_delete_user():
	username = request.form.get('username')
	return admin_dashboard.delete_user(username)

@app.route('/admin/view_analytics')
def admin_view_analytics():
	return admin_dashboard.view_analytics()

if __name__ == '__main__':
	app.run(debug=True)
