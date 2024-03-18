from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import uuid

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
	if not original_url:
		return jsonify({'error': 'URL is required'}), 400

	# Generate unique shortened URL
	short_url = custom_short if custom_short else str(uuid.uuid4())[:8]

	# Create URL object and store in DB
	url = URL(original=original_url, shortened=short_url, user=user, clicks=[], expiration=datetime.strptime(expiration, '%Y-%m-%dT%H:%M:%S'))
	DB[short_url] = url

	return jsonify({'shortened_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)

	# Check if URL exists and is not expired
	if not url or datetime.now() > url.expiration:
		return jsonify({'error': 'URL not found or expired'}), 404

	# Redirect to original URL and record click
	url.clicks.append({'timestamp': datetime.now().isoformat()})
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	user = request.args.get('user')
	urls = [url for url in DB.values() if url.user == user]

	return jsonify({'urls': urls}), 200

@app.route('/admin', methods=['GET'])
def get_admin():
	return jsonify({'urls': list(DB.values())}), 200

if __name__ == '__main__':
	app.run(debug=True)
