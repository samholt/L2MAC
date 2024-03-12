from flask import Flask, redirect, request, jsonify
from url_shortener import URLShortener
from user import User
from admin import Admin
from analytics import Analytics
from database import Database
from datetime import datetime, timedelta

app = Flask(__name__)
db = Database()
url_shortener = URLShortener(db)
user = User()
admin = Admin()
analytics = Analytics()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	expiration_date = datetime.strptime(data.get('expiration_date'), '%Y-%m-%dT%H:%M:%S') if data.get('expiration_date') else None
	short_url = url_shortener.shorten_url(original_url, expiration_date)
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>')
def redirect_to_url(short_url):
	original_url = url_shortener.get_original_url(short_url)
	if original_url:
		analytics.track_url(short_url)
		return redirect(original_url, code=302)
	else:
		return 'URL not found', 404

@app.route('/user/<username>/urls')
def get_user_urls(username):
	user_data = user.get_user_data(username)
	if user_data:
		return jsonify(user_data.get('urls', []))
	else:
		return 'User not found', 404

@app.route('/user/<username>/analytics')
def get_user_analytics(username):
	user_data = user.get_user_data(username)
	if user_data:
		urls = user_data.get('urls', [])
		analytics_data = {url: analytics.get_url_clicks(url) for url in urls}
		return jsonify(analytics_data)
	else:
		return 'User not found', 404

@app.route('/admin/dashboard')
def admin_dashboard():
	return jsonify(admin.get_system_performance())

if __name__ == '__main__':
	app.run(debug=True)
