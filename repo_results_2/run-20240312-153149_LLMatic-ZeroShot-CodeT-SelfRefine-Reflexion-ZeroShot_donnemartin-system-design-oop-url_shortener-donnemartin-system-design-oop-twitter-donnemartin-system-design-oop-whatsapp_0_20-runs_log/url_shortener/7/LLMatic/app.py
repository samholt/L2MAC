from flask import Flask, redirect, abort, request
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

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	short_url = url_shortener.generate_short_url(url)
	return {'short_url': short_url}, 200

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = url_shortener.get_original_url(short_url)
	if url:
		analytics.track_click(short_url, request.remote_addr)
		return redirect(url, code=302)
	else:
		abort(404)

@app.route('/analytics/<short_url>')
def get_analytics(short_url):
	data = analytics.get_analytics(short_url)
	return {'data': data}, 200

@app.route('/create_account', methods=['POST'])
def create_account():
	username = request.json.get('username')
	user_accounts.create_account(username)
	return {'message': 'Account created'}, 200

@app.route('/admin/dashboard')
def admin_dashboard_route():
	urls = admin_dashboard.view_all_urls()
	users = user_accounts.USER_DB
	analytics_data = analytics.ANALYTICS_DB
	performance = admin_dashboard.system_performance()
	return {'urls': urls, 'users': users, 'analytics': analytics_data, 'performance': performance}, 200

if __name__ == '__main__':
	app.run(debug=True)
