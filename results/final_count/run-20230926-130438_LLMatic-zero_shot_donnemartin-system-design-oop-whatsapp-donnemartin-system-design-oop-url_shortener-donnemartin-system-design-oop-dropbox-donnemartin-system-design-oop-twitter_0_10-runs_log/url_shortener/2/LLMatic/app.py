from flask import Flask, redirect, url_for, request
from url_shortener import get_original_url, delete_url, get_all_urls, generate_short_url, validate_url
from user_accounts import UserAccount
from analytics import get_system_performance, get_analytics, track_click

app = Flask(__name__)

user_account = UserAccount()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_original_url(short_url):
	original_url = get_original_url(short_url)
	if original_url is None:
		return 'URL not found', 404
	else:
		track_click(short_url, request.remote_addr)
		return redirect(original_url)

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.form.get('url')
	if not validate_url(url):
		return 'Invalid URL', 400
	short_url = generate_short_url(url)
	username = request.form.get('username')
	if username:
		user_account.add_url(username, short_url)
	return {'short_url': short_url}

@app.route('/analytics/<short_url>')
def view_analytics(short_url):
	return {'analytics': get_analytics(short_url)}

@app.route('/account', methods=['POST'])
def manage_account():
	action = request.form.get('action')
	username = request.form.get('username')
	if action == 'create':
		password = request.form.get('password')
		return {'message': user_account.create_account(username, password)}
	elif action == 'view_urls':
		return {'urls': user_account.view_urls(username)}
	elif action == 'delete':
		return {'message': user_account.delete_account(username)}

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
	if request.method == 'POST':
		action = request.form.get('action')
		if action == 'delete_url':
			short_url = request.form.get('short_url')
			delete_url(short_url)
		elif action == 'delete_user':
			username = request.form.get('username')
			user_account.delete_account(username)
		return redirect(url_for('admin_dashboard'))
	else:
		all_urls = get_all_urls()
		all_users = user_account.get_all_users()
		performance_data = get_system_performance()
		return {'urls': all_urls, 'users': all_users, 'performance': performance_data}

if __name__ == '__main__':
	app.run(debug=True)
