from flask import Flask, redirect, jsonify, request
from url_shortener import mock_db, generate_short_url, validate_url, is_expired
from user_accounts import UserAccount
from analytics import analytics_data, track_click, get_click_data

app = Flask(__name__)

user_account = UserAccount()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_original_url(short_url):
	if is_expired(short_url):
		return 'URL expired', 404
	original_url = mock_db.get(short_url)
	if original_url:
		return redirect(original_url)
	return 'URL not found', 404

@app.route('/admin/urls')
def view_all_urls():
	return jsonify(mock_db)

@app.route('/admin/delete_url/<short_url>')
def delete_url(short_url):
	if short_url in mock_db:
		del mock_db[short_url]
		return 'URL deleted successfully'
	return 'URL not found', 404

@app.route('/admin/delete_user/<username>')
def delete_user(username):
	if username in user_account.users:
		del user_account.users[username]
		return 'User deleted successfully'
	return 'User not found', 404

@app.route('/admin/analytics')
def view_analytics():
	return jsonify(analytics_data)

@app.route('/generate', methods=['POST'])
def generate():
	data = request.get_json()
	url = data.get('url')
	custom_short_link = data.get('custom_short_link')
	expiration_date = data.get('expiration_date')
	short_url = generate_short_url(url, custom_short_link, expiration_date)
	return jsonify({'short_url': short_url})

if __name__ == '__main__':
	app.run(debug=True)
