from flask import Flask, redirect, url_for, request, jsonify
import url_shortener
from user_accounts import UserAccounts
import analytics

app = Flask(__name__)

# Mock database
url_db = {}
user_accounts = UserAccounts()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_url(short_url):
	if short_url in url_db:
		return redirect(url_db[short_url])
	else:
		return 'URL not found', 404

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = data['url']
	custom_short_link = data.get('custom_short_link')
	expiration_time = data.get('expiration_time')
	short_url = url_shortener.generate_short_url(url, custom_short_link, expiration_time)
	url_db[short_url] = url
	return jsonify({'short_url': short_url})

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	username = data['username']
	return jsonify({'message': user_accounts.create_account(username)})

@app.route('/view_urls', methods=['POST'])
def view_urls():
	data = request.get_json()
	username = data['username']
	return jsonify(user_accounts.view_urls(username))

@app.route('/edit_url', methods=['POST'])
def edit_url():
	data = request.get_json()
	username = data['username']
	old_url = data['old_url']
	new_url = data['new_url']
	message = user_accounts.edit_url(username, old_url, new_url)
	if message == 'URL edited successfully.':
		url_db[new_url] = url_db.pop(old_url)
	return jsonify({'message': message})

@app.route('/delete_url', methods=['POST'])
def delete_url():
	data = request.get_json()
	username = data['username']
	url = data['url']
	return jsonify({'message': user_accounts.delete_url(username, url)})

@app.route('/view_statistics', methods=['POST'])
def view_statistics():
	data = request.get_json()
	short_url = data['short_url']
	return jsonify(analytics.get_statistics(short_url))

@app.route('/admin/view_urls')
def admin_view_urls():
	return jsonify(user_accounts.users)

@app.route('/admin/delete_url', methods=['POST'])
def admin_delete_url():
	data = request.get_json()
	username = data['username']
	url = data['url']
	return jsonify({'message': user_accounts.delete_url(username, url)})

@app.route('/admin/delete_user', methods=['POST'])
def admin_delete_user():
	data = request.get_json()
	username = data['username']
	if username in user_accounts.users:
		del user_accounts.users[username]
		return jsonify({'message': 'User deleted successfully.'})
	else:
		return 'User not found', 404

@app.route('/admin/view_analytics')
def admin_view_analytics():
	analytics_data = {}
	for username in user_accounts.users:
		analytics_data[username] = user_accounts.view_analytics(username)
	return jsonify(analytics_data)

if __name__ == '__main__':
	app.run(debug=True)
