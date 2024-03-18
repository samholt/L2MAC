from flask import Flask, request, redirect, jsonify
from mock_db import MockDB
import requests

app = Flask(__name__)
db = MockDB()

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	custom_short_link = request.json.get('custom_short_link')
	username = request.json.get('username')
	
	# Validate the URL
	try:
		response = requests.get(url)
		response.raise_for_status()
	except (requests.exceptions.RequestException, ValueError):
		return jsonify({'error': 'Invalid URL'}), 400
	
	# Add the URL to the database
	short_url = db.add_url(url, custom_short_link, username)
	if not short_url:
		return jsonify({'error': 'Custom short link not available'}), 400
	
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = db.get_url(short_url)
	if url:
		return redirect(url)
	else:
		return 'URL not found', 404

@app.route('/analytics/<username>', methods=['GET'])
def analytics(username):
	analytics_data = db.get_user_analytics(username)
	if analytics_data:
		return jsonify(analytics_data)
	else:
		return 'Analytics not found', 404

@app.route('/account', methods=['GET', 'POST', 'PUT', 'DELETE'])
def account():
	if request.method == 'POST':
		username = request.json.get('username')
		password = request.json.get('password')
		return jsonify({'message': db.create_account(username, password)}), 201
	elif request.method == 'GET':
		username = request.json.get('username')
		return jsonify(db.get_user_urls(username)), 200
	elif request.method == 'PUT':
		username = request.json.get('username')
		old_short_url = request.json.get('old_short_url')
		new_short_url = request.json.get('new_short_url')
		return jsonify({'message': db.update_url(username, old_short_url, new_short_url)}), 200
	elif request.method == 'DELETE':
		username = request.json.get('username')
		short_url = request.json.get('short_url')
		return jsonify({'message': db.delete_url(username, short_url)}), 200

@app.route('/admin', methods=['GET', 'DELETE'])
def admin():
	if request.method == 'GET':
		return jsonify(db.get_admin_dashboard()), 200
	elif request.method == 'DELETE':
		username = request.json.get('username')
		short_url = request.json.get('short_url')
		return jsonify({'message': db.delete_admin(username, short_url)}), 200

if __name__ == '__main__':
	app.run(debug=True)
