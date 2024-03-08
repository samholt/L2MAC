import string
import random
from flask import Flask, request, redirect, jsonify
from urllib.parse import urlparse
from datetime import datetime

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'urls': {},
	'analytics': {},
	'expiration': {}
}

@app.route('/')
def home():
	short_url = request.args.get('url')
	if short_url in DATABASE['urls']:
		# Check if URL is expired
		if short_url in DATABASE['expiration'] and datetime.now() > DATABASE['expiration'][short_url]:
			return 'URL expired', 410
		# Update analytics
		if short_url not in DATABASE['analytics']:
			DATABASE['analytics'][short_url] = []
		DATABASE['analytics'][short_url].append({'timestamp': datetime.now().isoformat(), 'location': 'Unknown'})
		return redirect(DATABASE['urls'][short_url])
	else:
		return 'URL not found', 404

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	custom_alias = request.json.get('custom_alias')
	username = request.json.get('username')
	expiration = request.json.get('expiration')

	if not url:
		return jsonify({'error': 'URL is required'}), 400

	if not urlparse(url).scheme:
		return jsonify({'error': 'Invalid URL'}), 400

	if username and username not in DATABASE['users']:
		return jsonify({'error': 'User not found'}), 404

	if custom_alias:
		if custom_alias in DATABASE['urls']:
			return jsonify({'error': 'Custom alias already in use'}), 400
		else:
			DATABASE['urls'][custom_alias] = url
			if username:
				DATABASE['users'][username]['urls'].append(custom_alias)
			if expiration:
				DATABASE['expiration'][custom_alias] = datetime.fromisoformat(expiration)
			return jsonify({'short_url': custom_alias}), 200

	short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	while short_url in DATABASE['urls']:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

	DATABASE['urls'][short_url] = url
	if username:
		DATABASE['users'][username]['urls'].append(short_url)
	if expiration:
		DATABASE['expiration'][short_url] = datetime.fromisoformat(expiration)
	return jsonify({'short_url': short_url}), 200

@app.route('/analytics', methods=['GET'])
def analytics():
	short_url = request.args.get('url')
	if short_url in DATABASE['analytics']:
		return jsonify(DATABASE['analytics'][short_url])
	else:
		return jsonify([])

@app.route('/account', methods=['GET', 'POST', 'PUT', 'DELETE'])
def account():
	if request.method == 'POST':
		username = request.json.get('username')
		if username in DATABASE['users']:
			return jsonify({'error': 'Username already exists'}), 400
		DATABASE['users'][username] = {'urls': []}
		return jsonify({'message': 'Account created'}), 200

	elif request.method == 'GET':
		username = request.args.get('username')
		if username in DATABASE['users']:
			return jsonify(DATABASE['users'][username])
		else:
			return jsonify({'error': 'User not found'}), 404

	elif request.method == 'PUT':
		username = request.json.get('username')
		new_url = request.json.get('new_url')
		old_url = request.json.get('old_url')
		if username in DATABASE['users'] and old_url in DATABASE['users'][username]['urls']:
			DATABASE['users'][username]['urls'].remove(old_url)
			DATABASE['users'][username]['urls'].append(new_url)
			DATABASE['urls'][new_url] = DATABASE['urls'][old_url]
			del DATABASE['urls'][old_url]
			return jsonify({'message': 'URL updated'}), 200
		else:
			return jsonify({'error': 'User or URL not found'}), 404

	elif request.method == 'DELETE':
		username = request.json.get('username')
		url = request.json.get('url')
		if username in DATABASE['users'] and url in DATABASE['users'][username]['urls']:
			DATABASE['users'][username]['urls'].remove(url)
			del DATABASE['urls'][url]
			return jsonify({'message': 'URL deleted'}), 200
		else:
			return jsonify({'error': 'User or URL not found'}), 404

@app.route('/admin', methods=['GET', 'DELETE'])
def admin():
	if request.method == 'GET':
		return jsonify({'users': DATABASE['users'], 'urls': DATABASE['urls'], 'analytics': DATABASE['analytics']})
	elif request.method == 'DELETE':
		username = request.json.get('username')
		url = request.json.get('url')
		if username and username in DATABASE['users']:
			del DATABASE['users'][username]
			return jsonify({'message': 'User deleted'}), 200
		elif url and url in DATABASE['urls']:
			del DATABASE['urls'][url]
			return jsonify({'message': 'URL deleted'}), 200
		else:
			return jsonify({'error': 'User or URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
