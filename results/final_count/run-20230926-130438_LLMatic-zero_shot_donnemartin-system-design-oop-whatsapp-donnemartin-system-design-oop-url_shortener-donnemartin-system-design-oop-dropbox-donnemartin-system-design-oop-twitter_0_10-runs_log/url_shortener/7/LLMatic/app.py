from flask import Flask, request, jsonify, redirect
from url_shortener import generate_short_url, validate_url, get_url
from analytics import track_click, get_statistics
from user_accounts import UserAccount
from admin_dashboard import AdminDashboard

app = Flask(__name__)

# Mock databases
url_db = {}
analytics_db = {}
user_account = UserAccount()
admin_dashboard = AdminDashboard()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = data.get('url')
	custom_short_url = data.get('custom_short_url')
	expiration = data.get('expiration')
	if validate_url(url):
		short_url = generate_short_url(url, custom_short_url, expiration)
		return jsonify({'short_url': short_url})
	else:
		return jsonify({'error': 'Invalid URL'}), 400

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = get_url(short_url)
	if url:
		track_click(short_url, request.remote_addr)
		return redirect(url, code=302)
	else:
		return 'URL not found', 404

@app.route('/analytics/<short_url>')
def analytics(short_url):
	return jsonify(get_statistics(short_url))

@app.route('/create_account', methods=['POST'])
def create_account():
	username = request.get_json().get('username')
	return jsonify({'message': user_account.create_account(username)})

@app.route('/admin/view_all_urls')
def view_all_urls():
	return jsonify(admin_dashboard.view_all_urls())

if __name__ == '__main__':
	app.run(debug=True)
