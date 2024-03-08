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
	clicks: int
	click_data: list
	expiration: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user = data.get('user')
	expiration = data.get('expiration')
	shortened_url = str(uuid.uuid4())[:8]
	url = URL(original_url, shortened_url, user, 0, [], expiration)
	DB[shortened_url] = url
	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	url = DB.get(shortened_url)
	if url and (not url.expiration or url.expiration > datetime.now()):
		url.clicks += 1
		url.click_data.append({'click_time': datetime.now().isoformat()})
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

@app.route('/analytics/<shortened_url>', methods=['GET'])
def get_analytics(shortened_url):
	url = DB.get(shortened_url)
	if url:
		return jsonify({'original_url': url.original, 'clicks': url.clicks, 'click_data': url.click_data}), 200
	else:
		return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
