from flask import Flask, request, redirect, jsonify
import uuid
import requests
from datetime import datetime

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'urls': {},
	'analytics': {}
}

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	custom_url = data.get('custom_url')
	username = data.get('username')
	expiration_date = data.get('expiration_date')

	# Validate URL
	try:
		response = requests.get(original_url)
		response.raise_for_status()
	except (requests.RequestException, ValueError):
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate short URL
	short_url = custom_url if custom_url and custom_url not in DATABASE['urls'] else str(uuid.uuid4())[:8]
	DATABASE['urls'][short_url] = {'url': original_url, 'username': username, 'expiration_date': expiration_date}
	DATABASE['analytics'][short_url] = {'clicks': 0, 'click_details': []}
	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url_data = DATABASE['urls'].get(short_url)
	if url_data:
		if url_data.get('expiration_date') and datetime.now() > datetime.fromisoformat(url_data['expiration_date']):
			return 'URL expired', 410
		original_url = url_data['url']
		DATABASE['analytics'][short_url]['clicks'] += 1
		DATABASE['analytics'][short_url]['click_details'].append({'timestamp': datetime.now().isoformat(), 'location': request.remote_addr})
		return redirect(original_url)
	else:
		return 'URL not found', 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	username = request.args.get('username')
	user_urls = {k: v for k, v in DATABASE['urls'].items() if v['username'] == username}
	user_analytics = {k: DATABASE['analytics'][k] for k in user_urls.keys()}
	return jsonify(user_analytics), 200

@app.route('/account', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_account():
	if request.method == 'POST':
		data = request.get_json()
		username = data.get('username')
		DATABASE['users'][username] = data
		return jsonify({'message': 'Account created'}), 201
	elif request.method == 'GET':
		username = request.args.get('username')
		user_urls = {k: v for k, v in DATABASE['urls'].items() if v['username'] == username}
		return jsonify(user_urls), 200
	elif request.method == 'PUT':
		data = request.get_json()
		short_url = data.get('short_url')
		new_url = data.get('new_url')
		username = data.get('username')
		if DATABASE['urls'].get(short_url) and DATABASE['urls'][short_url]['username'] == username:
			DATABASE['urls'][short_url]['url'] = new_url
			return jsonify({'message': 'URL updated'}), 200
		else:
			return jsonify({'error': 'URL not found or not owned by user'}), 404
	elif request.method == 'DELETE':
		data = request.get_json()
		short_url = data.get('short_url')
		username = data.get('username')
		if DATABASE['urls'].get(short_url) and DATABASE['urls'][short_url]['username'] == username:
			del DATABASE['urls'][short_url]
			del DATABASE['analytics'][short_url]
			return jsonify({'message': 'URL deleted'}), 200
		else:
			return jsonify({'error': 'URL not found or not owned by user'}), 404

@app.route('/admin', methods=['GET', 'DELETE'])
def admin_dashboard():
	if request.method == 'GET':
		return jsonify(DATABASE), 200
	elif request.method == 'DELETE':
		data = request.get_json()
		short_url = data.get('short_url')
		username = data.get('username')
		if DATABASE['urls'].get(short_url):
			del DATABASE['urls'][short_url]
			del DATABASE['analytics'][short_url]
			return jsonify({'message': 'URL deleted'}), 200
		elif DATABASE['users'].get(username):
			del DATABASE['users'][username]
			return jsonify({'message': 'User account deleted'}), 200
		else:
			return jsonify({'error': 'URL or user account not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
