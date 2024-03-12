from flask import Flask, redirect, abort, request, jsonify
from url_shortener import url_db
from user_accounts import UserAccounts
from analytics import analytics_db, get_statistics

app = Flask(__name__)
user_accounts = UserAccounts()

@app.route('/')
def home():
	return 'Hello, World!', 200

@app.route('/<short_url>')
def redirect_to_url(short_url):
	if short_url in url_db:
		return redirect(url_db[short_url])
	else:
		abort(404)

@app.route('/admin/view_urls')
def view_all_urls():
	if not url_db:
		return 'No URLs found.', 404
	return jsonify(list(url_db.keys())), 200

@app.route('/admin/delete_url', methods=['POST'])
def delete_url():
	short_url = request.form.get('short_url')
	if short_url in url_db:
		del url_db[short_url]
		return 'URL deleted successfully.', 200
	else:
		return 'URL not found.', 404

@app.route('/admin/delete_user', methods=['POST'])
def delete_user():
	username = request.form.get('username')
	if username in user_accounts.users:
		del user_accounts.users[username]
		return 'User deleted successfully.', 200
	else:
		return 'User not found.', 404

@app.route('/admin/view_analytics/<short_url>')
def view_analytics(short_url):
	if short_url in analytics_db:
		return jsonify(get_statistics(short_url)), 200
	else:
		return 'URL not found in analytics.', 404

if __name__ == '__main__':
	app.run(debug=True)
