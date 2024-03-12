from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import pytz
import uuid

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original: str
	shortened: str
	clicks: int
	click_data: list
	expiration: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	for url in DB.values():
		if url.original == original_url:
			return jsonify({'shortened_url': url.shortened}), 200
	shortened_url = data.get('custom') or str(uuid.uuid4())[:8]
	if shortened_url in DB:
		return jsonify({'error': 'Custom URL is already in use'}), 400
	expiration = data.get('expiration')
	if expiration:
		expiration = datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S')
	DB[shortened_url] = URL(original_url, shortened_url, 0, [], expiration)
	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	url = DB.get(shortened_url)
	if not url or (url.expiration and url.expiration < datetime.now(pytz.UTC)):
		return jsonify({'error': 'URL not found or expired'}), 404
	url.clicks += 1
	url.click_data.append({'timestamp': datetime.now(pytz.UTC).isoformat()})
	return redirect(url.original, code=302)

@app.route('/analytics/<shortened_url>', methods=['GET'])
def get_analytics(shortened_url):
	url = DB.get(shortened_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	return jsonify({'original_url': url.original, 'clicks': url.clicks, 'click_data': url.click_data}), 200

if __name__ == '__main__':
	app.run(debug=True)
