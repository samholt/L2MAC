from flask import Flask, redirect, url_for, jsonify
from services.url_shortener import UrlShortener
from services.user_accounts import UserAccounts
from services.analytics import Analytics

# Initialize Flask application
app = Flask(__name__)

# Initialize services
url_shortener = UrlShortener()
user_accounts = UserAccounts()
analytics = Analytics()

@app.route('/')
def hello_world():
	# Default route
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_url(short_url):
	# Redirect to original URL based on short URL
	original_url = url_shortener.get_original_url(short_url)
	if original_url == 'URL not found' or original_url == 'URL expired':
		return original_url, 404
	return redirect(original_url)

@app.route('/admin/urls')
def view_all_urls():
	# View all short URLs
	return jsonify(url_shortener.get_all_urls())

@app.route('/admin/delete_url/<short_url>')
def delete_url(short_url):
	# Delete a short URL
	return url_shortener.delete_url(short_url)

@app.route('/admin/delete_account/<username>')
def delete_account(username):
	# Delete a user account
	return user_accounts.delete_account(username)

@app.route('/admin/analytics')
def view_analytics():
	# View analytics data
	return jsonify(analytics.get_all_data())

if __name__ == '__main__':
	# Run the application
	app.run()

