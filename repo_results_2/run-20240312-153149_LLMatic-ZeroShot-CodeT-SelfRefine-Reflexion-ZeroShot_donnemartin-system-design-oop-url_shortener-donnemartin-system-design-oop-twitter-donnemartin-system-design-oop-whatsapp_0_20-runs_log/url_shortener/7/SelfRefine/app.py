from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import string
import random
import requests

app = Flask(__name__)

# Mock database
DB = {}

# Mock user database
USERS = {}

# Mock admin database
ADMINS = {}

# Mock analytics database
ANALYTICS = {}

# URL validation function
def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False

# URL shortening function
def shorten_url(url):
	short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	while short_url in DB:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	DB[short_url] = url
	ANALYTICS[short_url] = 0
	return short_url

# URL redirection function
@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	if short_url not in DB:
		return 'URL not found', 404
	else:
		ANALYTICS[short_url] += 1
		return redirect(DB[short_url])

# URL shortening endpoint
@app.route('/shorten', methods=['POST'])
def url_shortening():
	data = request.get_json()
	url = data.get('url')
	if not validate_url(url):
		return 'Invalid URL', 400
	short_url = shorten_url(url)
	return jsonify({'short_url': short_url}), 200

# Analytics endpoint
@app.route('/analytics', methods=['GET'])
def get_analytics():
	return jsonify(ANALYTICS), 200

if __name__ == '__main__':
	app.run(debug=True)
