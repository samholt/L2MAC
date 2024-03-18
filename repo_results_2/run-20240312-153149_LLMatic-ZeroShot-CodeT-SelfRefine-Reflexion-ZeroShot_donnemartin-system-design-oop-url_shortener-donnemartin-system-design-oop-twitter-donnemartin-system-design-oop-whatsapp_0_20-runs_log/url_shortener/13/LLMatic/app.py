from flask import Flask, redirect, url_for, request
import url_shortener
import user_accounts
import analytics

app = Flask(__name__)

user_accounts = user_accounts.UserAccounts()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = url_shortener.url_database.get(short_url)
	if url:
		return redirect(url)
	else:
		return 'URL not found', 404

@app.route('/admin/dashboard')
def admin_dashboard():
	if request.method == 'GET':
		return {'urls': url_shortener.url_database, 'users': user_accounts.users}

@app.route('/admin/delete_url/<short_url>', methods=['DELETE'])
def delete_url(short_url):
	if short_url in url_shortener.url_database:
		del url_shortener.url_database[short_url]
		return {'message': 'URL deleted successfully'}
	else:
		return {'message': 'URL not found'}, 404

@app.route('/admin/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
	if user_accounts.delete_user(username):
		return {'message': 'User deleted successfully'}
	else:
		return {'message': 'User not found'}, 404

@app.route('/admin/analytics')
def analytics_dashboard():
	return analytics.get_system_performance()

if __name__ == '__main__':
	app.run(debug=True)
