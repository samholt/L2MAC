from datetime import datetime
from flask import Flask, request, jsonify
from models import User, URL, Analytics
from utils import validate_url, generate_short_link

app = Flask(__name__)

users = {}
urls = {}
analytics = {}

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	if 'username' in data and 'password' in data:
		user = User.create(len(users) + 1, data['username'], data['password'])
		users[user.id] = user
		return jsonify(user.get_details()), 201
	return jsonify({'message': 'Invalid request. Please provide username and password.'}), 400

@app.route('/authenticate', methods=['POST'])
def authenticate():
	data = request.get_json()
	if 'username' in data and 'password' in data:
		for user in users.values():
			if user.authenticate(data['username'], data['password']):
				return jsonify(user.get_details()), 200
	return jsonify({'message': 'Invalid credentials. Please check your username and password.'}), 401

@app.route('/submit_url', methods=['POST'])
def submit_url():
	data = request.get_json()
	if 'original_url' in data and 'user_id' in data and int(data['user_id']) in users:
		if validate_url(data['original_url']):
			short_url = generate_short_link()
			url = URL.create(data['original_url'], short_url, users[int(data['user_id'])])
			urls[short_url] = url
			return jsonify(url.get_details()), 201
	return jsonify({'message': 'Invalid request. Please provide a valid URL and a valid user ID.'}), 400

@app.route('/<short_url>', methods=['GET'])
def access_url(short_url):
	if short_url in urls:
		if datetime.now() > urls[short_url].expiration_date:
			urls[short_url].delete()
			del urls[short_url]
			return jsonify({'message': 'URL expired.'}), 410
		analytics_entry = Analytics.create(urls[short_url], datetime.now(), request.remote_addr)
		analytics[short_url] = analytics_entry
		return jsonify({'original_url': urls[short_url].original_url}), 302
	return jsonify({'message': 'URL not found. Please check the shortened URL.'}), 404

@app.route('/user_urls/<user_id>', methods=['GET'])
def user_urls(user_id):
	if int(user_id) in users:
		user_urls = [url.get_details() for url in urls.values() if url.user.id == int(user_id)]
		return jsonify(user_urls), 200
	return jsonify({'message': 'User not found. Please check the user ID.'}), 404

@app.route('/url_analytics/<short_url>', methods=['GET'])
def url_analytics(short_url):
	if short_url in analytics:
		return jsonify(analytics[short_url].get_details()), 200
	return jsonify({'message': 'URL not found. Please check the shortened URL.'}), 404

@app.route('/edit_url/<short_url>', methods=['PUT'])
def edit_url(short_url):
	data = request.get_json()
	if 'original_url' in data and 'user_id' in data and int(data['user_id']) in users and short_url in urls and urls[short_url].user.id == int(data['user_id']):
		if validate_url(data['original_url']):
			urls[short_url].update_original_url(data['original_url'])
			return jsonify(urls[short_url].get_details()), 200
	return jsonify({'message': 'Invalid request. Please provide a valid URL, a valid user ID, and a valid shortened URL.'}), 400

@app.route('/delete_url/<short_url>', methods=['DELETE'])
def delete_url(short_url):
	data = request.get_json()
	if 'user_id' in data and int(data['user_id']) in users and short_url in urls and urls[short_url].user.id == int(data['user_id']):
		urls[short_url].delete()
		del urls[short_url]
		return jsonify({'message': 'URL deleted successfully.'}), 200
	return jsonify({'message': 'Invalid request. Please provide a valid user ID and a valid shortened URL.'}), 400

# Admin routes
@app.route('/admin/urls', methods=['GET'])
def admin_urls():
	return jsonify([url.get_details() for url in urls.values()]), 200

@app.route('/admin/delete_url/<short_url>', methods=['DELETE'])
def admin_delete_url(short_url):
	if short_url in urls:
		urls[short_url].delete()
		del urls[short_url]
		return jsonify({'message': 'URL deleted successfully.'}), 200
	return jsonify({'message': 'URL not found. Please check the shortened URL.'}), 404

@app.route('/admin/delete_user/<user_id>', methods=['DELETE'])
def admin_delete_user(user_id):
	if int(user_id) in users:
		del users[int(user_id)]
		return jsonify({'message': 'User deleted successfully.'}), 200
	return jsonify({'message': 'User not found. Please check the user ID.'}), 404

@app.route('/admin/analytics', methods=['GET'])
def admin_analytics():
	return jsonify([entry.get_details() for entry in analytics.values()]), 200

if __name__ == '__main__':
	app.run(debug=True)
