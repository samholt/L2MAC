from flask import Flask, redirect, url_for, request
import url_shortener as us
import analytics as an
import user_accounts as ua
import admin_dashboard as ad

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_url(short_url):
	url = us.get_original_url(short_url)
	if url:
		an.record_click(short_url, request.remote_addr)
		return redirect(url)
	else:
		return 'URL not found', 404

@app.route('/generate', methods=['POST'])
def generate_url():
	url = request.form.get('url')
	expiration_minutes = request.form.get('expiration_minutes', 0)
	short_url = us.generate_short_url(url, expiration_minutes)
	return short_url

@app.route('/custom', methods=['POST'])
def custom_url():
	url = request.form.get('url')
	custom_link = request.form.get('custom_link')
	expiration_minutes = request.form.get('expiration_minutes', 0)
	short_url = us.custom_short_link(url, custom_link, expiration_minutes)
	return short_url

@app.route('/analytics/<short_url>')
def analytics(short_url):
	return an.get_analytics(short_url)

@app.route('/account/create', methods=['POST'])
def create_account():
	username = request.form.get('username')
	password = request.form.get('password')
	return ua.USER_ACCOUNTS.create_account(username, password)

@app.route('/account/view/<username>')
def view_urls(username):
	return ua.USER_ACCOUNTS.view_urls(username)

@app.route('/admin/view')
def view_all_urls():
	return ad.view_all_urls()

if __name__ == '__main__':
	app.run(debug=True)
