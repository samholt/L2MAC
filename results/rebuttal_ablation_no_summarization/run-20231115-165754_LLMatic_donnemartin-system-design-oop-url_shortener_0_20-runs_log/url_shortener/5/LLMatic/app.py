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
	custom_short_url = data.get('custom_short_url')
	username = data.get('username')
	expiration_date = data.get('expiration_date')

	# Validate URL
	try:
		response = requests.get(original_url)
		response.raise_for_status()
	except (requests.RequestException, ValueError):
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate or use custom short URL
	short_url = custom_short_url if custom_short_url and custom_short_url not in DATABASE['urls'] else str(uuid.uuid4())[:8]
	DATABASE['urls'][short_url] = {'original_url': original_url, 'expiration_date': expiration_date}
	DATABASE['analytics'][short_url] = {'clicks': 0, 'click_details': []}

	# Associate the shortened URL with the user
	if username in DATABASE['users']:
		DATABASE['users'][username]['urls'].append(short_url)

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url_data = DATABASE['urls'].get(short_url)
	if url_data:
		# Check if the URL has expired
		if url_data['expiration_date'] and datetime.now() > datetime.fromisoformat(url_data['expiration_date']):
			return 'URL has expired', 410
		# Update analytics
		DATABASE['analytics'][short_url]['clicks'] += 1
		DATABASE['analytics'][short_url]['click_details'].append({'timestamp': datetime.now().isoformat(), 'location': 'Dummy Location'})
		return redirect(url_data['original_url'])
	else:
		return 'URL not found', 404

@app.route('/analytics', methods=['GET'])
def view_analytics():
	return jsonify(DATABASE['analytics']), 200

@app.route('/account', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_account():
	if request.method == 'POST':
		data = request.get_json()
		username = data.get('username')
		DATABASE['users'][username] = {'urls': [], 'analytics': {}}
		return jsonify({'message': 'Account created'}), 201
	elif request.method == 'GET':
		username = request.args.get('username')
		if username in DATABASE['users']:
			return jsonify(DATABASE['users'][username]), 200
		else:
			return jsonify({'error': 'User not found'}), 404
	elif request.method == 'PUT':
		data = request.get_json()
		username = data.get('username')
		short_url = data.get('short_url')
		new_url = data.get('new_url')
		if username in DATABASE['users'] and short_url in DATABASE['users'][username]['urls']:
			DATABASE['urls'][short_url]['original_url'] = new_url
			return jsonify({'message': 'URL updated'}), 200
		else:
			return jsonify({'error': 'User or URL not found'}), 404
	elif request.method == 'DELETE':
		data = request.get_json()
		username = data.get('username')
		short_url = data.get('short_url')
		if username in DATABASE['users'] and short_url in DATABASE['users'][username]['urls']:
			DATABASE['users'][username]['urls'].remove(short_url)
			del DATABASE['urls'][short_url]
			return jsonify({'message': 'URL deleted'}), 200
		else:
			return jsonify({'error': 'User or URL not found'}), 404

@app.route('/admin', methods=['GET', 'DELETE'])
def manage_admin():
	if request.method == 'GET':
		return jsonify(DATABASE), 200
	elif request.method == 'DELETE':
		data = request.get_json()
		username = data.get('username')
		short_url = data.get('short_url')
		if username in DATABASE['users']:
			del DATABASE['users'][username]
			return jsonify({'message': 'User deleted'}), 200
		elif short_url in DATABASE['urls']:
			del DATABASE['urls'][short_url]
			del DATABASE['analytics'][short_url]
			return jsonify({'message': 'URL deleted'}), 200
		else:
			return jsonify({'error': 'User or URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)

