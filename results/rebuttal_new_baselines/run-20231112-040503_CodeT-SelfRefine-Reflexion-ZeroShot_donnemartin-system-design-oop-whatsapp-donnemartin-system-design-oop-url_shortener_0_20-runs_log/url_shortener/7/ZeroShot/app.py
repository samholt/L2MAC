from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
import datetime
import random
import string

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original: str
	shortened: str
	clicks: int
	created_at: datetime.datetime
	expires_at: datetime.datetime
	owner: str

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	custom_alias = data.get('alias')
	expiration_date = data.get('expires_at')
	owner = data.get('owner')

	# Validate URL
	if not original_url:
		return jsonify({'error': 'URL is required'}), 400

	# Generate unique alias
	alias = custom_alias if custom_alias else ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

	# Check if alias already exists
	if alias in DB:
		return jsonify({'error': 'Alias already exists'}), 400

	# Create URL object
	url = URL(original=original_url, shortened=alias, clicks=0, created_at=datetime.datetime.now(), expires_at=expiration_date, owner=owner)

	# Save to DB
	DB[alias] = url

	return jsonify({'shortened_url': f'http://localhost:5000/{alias}'}), 201

@app.route('/<alias>', methods=['GET'])
def redirect_to_url(alias):
	url = DB.get(alias)

	# Check if URL exists
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if url.expires_at and url.expires_at < datetime.datetime.now():
		return jsonify({'error': 'URL has expired'}), 410

	# Increment click count
	url.clicks += 1

	# Redirect to original URL
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	alias = data.get('alias')

	# Check if URL exists
	if not alias in DB:
		return jsonify({'error': 'URL not found'}), 404

	url = DB[alias]

	# Return analytics
	return jsonify({'original_url': url.original, 'clicks': url.clicks, 'created_at': url.created_at, 'expires_at': url.expires_at}), 200

if __name__ == '__main__':
	app.run(debug=True)
