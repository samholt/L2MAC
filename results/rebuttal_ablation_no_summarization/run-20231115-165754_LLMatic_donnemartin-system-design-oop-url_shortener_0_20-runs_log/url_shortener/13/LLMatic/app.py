import hashlib
import requests
from flask import Flask, request, redirect, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'urls': {},
	'analytics': {},
	'expiration': {}
}

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	custom_alias = request.json.get('custom_alias')
	username = request.json.get('username')
	expiration_date = request.json.get('expiration_date')

	# Validate URL
	try:
		response = requests.get(url)
		response.raise_for_status()
	except (requests.exceptions.RequestException, ValueError):
		return jsonify({'message': 'Invalid URL'}), 400

	# Generate short URL
	short_url = hashlib.md5(url.encode()).hexdigest()[:10]

	# If custom alias is provided and not already in use, use it
	if custom_alias:
		if custom_alias in DATABASE['urls']:
			return jsonify({'message': 'Custom alias already in use'}), 400
		else:
			short_url = custom_alias

	# Store in database
	DATABASE['urls'][short_url] = url
	if expiration_date:
		DATABASE['expiration'][short_url] = expiration_date

	# Add to user's list of URLs if username is provided
	if username:
		if username not in DATABASE['users']:
			DATABASE['users'][username] = []
		DATABASE['users'][username].append(short_url)

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	# Check if short_url exists in database
	if short_url in DATABASE['urls']:
		# Check if the URL has expired
		if short_url in DATABASE['expiration'] and datetime.now() > datetime.fromisoformat(DATABASE['expiration'][short_url]):
			return jsonify({'message': 'URL has expired'}), 400
		# Redirect to the original URL
		# Update analytics
		if short_url not in DATABASE['analytics']:
			DATABASE['analytics'][short_url] = []
		DATABASE['analytics'][short_url].append({'click_time': datetime.now().isoformat(), 'location': 'Unknown'})
		return redirect(DATABASE['urls'][short_url], code=302)
	else:
		# Return error message if short_url does not exist
		return jsonify({'message': 'URL not found'}), 404

@app.route('/analytics/<short_url>', methods=['GET'])
def view_analytics(short_url):
	# Check if short_url exists in database
	if short_url in DATABASE['analytics']:
		# Return analytics data
		return jsonify(DATABASE['analytics'][short_url]), 200
	else:
		# Return error message if short_url does not exist
		return jsonify({'message': 'URL not found'}), 404

@app.route('/account', methods=['POST', 'PUT', 'DELETE'])
def manage_account():
	username = request.json.get('username')
	if request.method == 'POST':
		# Create account
		if username in DATABASE['users']:
			return jsonify({'message': 'Username already exists'}), 400
		else:
			DATABASE['users'][username] = []
			return jsonify({'message': 'Account created'}), 200
	elif request.method == 'PUT':
		# Edit account
		new_username = request.json.get('new_username')
		if username not in DATABASE['users']:
			return jsonify({'message': 'Username not found'}), 404
		elif new_username in DATABASE['users']:
			return jsonify({'message': 'New username already exists'}), 400
		else:
			DATABASE['users'][new_username] = DATABASE['users'].pop(username)
			return jsonify({'message': 'Account updated'}), 200
	elif request.method == 'DELETE':
		# Delete account
		if username not in DATABASE['users']:
			return jsonify({'message': 'Username not found'}), 404
		else:
			for url in DATABASE['users'][username]:
				if url in DATABASE['urls']:
					del DATABASE['urls'][url]
				if url in DATABASE['analytics']:
					del DATABASE['analytics'][url]
				if url in DATABASE['expiration']:
					del DATABASE['expiration'][url]
			del DATABASE['users'][username]
			return jsonify({'message': 'Account deleted'}), 200

@app.route('/admin', methods=['GET', 'DELETE'])
def admin_dashboard():
	if request.method == 'GET':
		# View all shortened URLs and users
		return jsonify({'users': DATABASE['users'], 'urls': DATABASE['urls']}), 200
	elif request.method == 'DELETE':
		# Delete a URL or user account
		username = request.json.get('username')
		short_url = request.json.get('short_url')
		if username:
			if username in DATABASE['users']:
				for url in DATABASE['users'][username]:
					if url in DATABASE['urls']:
						del DATABASE['urls'][url]
					if url in DATABASE['analytics']:
						del DATABASE['analytics'][url]
					if url in DATABASE['expiration']:
						del DATABASE['expiration'][url]
				del DATABASE['users'][username]
				return jsonify({'message': 'User deleted'}), 200
			else:
				return jsonify({'message': 'User not found'}), 404
		elif short_url:
			if short_url in DATABASE['urls']:
				del DATABASE['urls'][short_url]
				if short_url in DATABASE['analytics']:
					del DATABASE['analytics'][short_url]
				if short_url in DATABASE['expiration']:
					del DATABASE['expiration'][short_url]
				return jsonify({'message': 'URL deleted'}), 200
			else:
				return jsonify({'message': 'URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
