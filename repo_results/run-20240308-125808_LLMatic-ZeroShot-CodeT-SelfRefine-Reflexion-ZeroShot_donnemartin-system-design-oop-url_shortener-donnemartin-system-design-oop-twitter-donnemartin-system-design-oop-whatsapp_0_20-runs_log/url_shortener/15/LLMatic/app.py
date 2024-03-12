from flask import Flask, request, redirect, jsonify
from mock_db import MockDB
from urllib.parse import urlparse
from datetime import datetime
import requests

app = Flask(__name__)
db = MockDB()

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	custom_short_link = request.json.get('custom_short_link')
	expiration_date = request.json.get('expiration_date')
	if not validate_url(url):
		return 'Invalid URL', 400
	short_url = db.add_url(url, custom_short_link, expiration_date)
	if not short_url:
		return 'Custom short link is not available', 400
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url_data = db.get_url(short_url)
	if url_data:
		if 'expiration_date' in url_data and url_data['expiration_date'] and datetime.now() > datetime.fromisoformat(url_data['expiration_date']):
			return 'URL expired', 404
		return redirect(url_data['url'], code=302)
	else:
		return 'URL not found', 404

@app.route('/analytics/<short_url>', methods=['GET'])
def analytics(short_url):
	data = db.get_analytics(short_url)
	return jsonify(data), 200

@app.route('/account', methods=['GET', 'POST', 'PUT', 'DELETE'])
def account():
	if request.method == 'POST':
		username = request.json.get('username')
		password = request.json.get('password')
		user_id = db.add_user(username, password)
		return jsonify({'user_id': user_id}), 201
	elif request.method == 'GET':
		user_id = request.args.get('user_id')
		user = db.get_user(user_id)
		return jsonify(user), 200
	elif request.method == 'PUT':
		user_id = request.json.get('user_id')
		username = request.json.get('username')
		password = request.json.get('password')
		db.update_user(user_id, username, password)
		return 'User updated', 200
	elif request.method == 'DELETE':
		user_id = request.json.get('user_id')
		db.delete_user(user_id)
		return 'User deleted', 200

@app.route('/admin', methods=['GET', 'DELETE'])
def admin():
	if request.method == 'GET':
		data = db.get_admin_data()
		return jsonify(data), 200
	elif request.method == 'DELETE':
		user_id = request.json.get('user_id')
		short_url = request.json.get('short_url')
		if user_id:
			db.delete_user(user_id)
		if short_url:
			db.delete_url(short_url)
		return 'Deleted', 200

@app.route('/admin/analytics', methods=['GET'])
def admin_analytics():
	data = db.get_all_analytics()
	return jsonify(data), 200


def validate_url(url):
	try:
		result = urlparse(url)
		if all([result.scheme, result.netloc]):
			response = requests.get(url)
			return response.status_code == 200
		return False
	except ValueError:
		return False

if __name__ == '__main__':
	app.run(debug=True)
