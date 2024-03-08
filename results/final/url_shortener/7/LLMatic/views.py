from flask import Flask, redirect, request
from services import URLShortenerService

app = Flask(__name__)
url_shortener_service = URLShortenerService()

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	original_url = url_shortener_service.get_original_url(short_url)
	if original_url:
		return redirect(original_url, code=302)
	else:
		return 'URL not found', 404

@app.route('/shorten', methods=['POST'])
def shorten_url():
	original_url = request.form.get('original_url')
	user = request.form.get('user')
	custom_short_url = request.form.get('custom_short_url')
	short_url = url_shortener_service.generate_short_url(original_url, user, custom_short_url)
	return short_url

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	analytics = url_shortener_service.get_analytics(short_url)
	return analytics

@app.route('/register', methods=['POST'])
def register_user():
	username = request.form.get('username')
	password = request.form.get('password')
	message = url_shortener_service.create_user(username, password)
	return message

@app.route('/login', methods=['POST'])
def login_user():
	username = request.form.get('username')
	password = request.form.get('password')
	message = url_shortener_service.authenticate_user(username, password)
	return message

@app.route('/user/<username>/urls', methods=['GET'])
def get_user_urls(username):
	urls = url_shortener_service.get_user_urls(username)
	if isinstance(urls, list):
		return {'urls': urls}
	else:
		return urls, 404

@app.route('/admin/urls', methods=['GET'])
def get_all_urls():
	urls = url_shortener_service.get_all_urls()
	return {'urls': urls}

@app.route('/admin/delete_url/<short_url>', methods=['DELETE'])
def delete_url(short_url):
	message = url_shortener_service.delete_url(short_url)
	return message

@app.route('/admin/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
	message = url_shortener_service.delete_user(username)
	return message

