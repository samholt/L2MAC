from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import requests
from utils import generate_short_url

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: list
	expiration: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user = data.get('user')
	custom_short = data.get('custom')
	expiration = data.get('expiration')

	# Validate URL
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return jsonify({'error': 'Invalid URL'}), 400
	except:
		return jsonify({'error': 'Invalid URL'}), 400

	# Check if custom short URL is already in use
	if custom_short and custom_short in DB:
		return jsonify({'error': 'Custom short URL is already in use'}), 400

	# Generate short URL
	short_url = custom_short if custom_short else generate_short_url()

	# Create URL object and store in DB
	url = URL(original=original_url, shortened=short_url, user=user, clicks=[], expiration=expiration)
	DB[short_url] = url

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if not url or (url.expiration and url.expiration < datetime.now()):
		return jsonify({'error': 'URL not found or expired'}), 404

	# Redirect to original URL and log click
	url.clicks.append({'time': datetime.now(), 'location': request.remote_addr})
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	user = request.args.get('user')
	urls = [url for url in DB.values() if url.user == user]
	return jsonify({'urls': urls}), 200

@app.route('/admin', methods=['GET', 'DELETE'])
def admin_dashboard():
	if request.method == 'GET':
		return jsonify({'urls': list(DB.values())}), 200
	elif request.method == 'DELETE':
		url_to_delete = request.args.get('url')
		if url_to_delete in DB:
			del DB[url_to_delete]
			return jsonify({'message': 'URL deleted'}), 200
		else:
			return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
