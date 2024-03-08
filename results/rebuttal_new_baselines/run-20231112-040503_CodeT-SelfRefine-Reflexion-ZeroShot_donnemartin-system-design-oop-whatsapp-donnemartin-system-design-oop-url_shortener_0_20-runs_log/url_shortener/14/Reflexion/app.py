from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime, timedelta
import random
import string

app = Flask(__name__)

# Mock database
urls_db = {}

@dataclass
class URL:
	original_url: str
	short_url: str
	expiration_date: datetime = None

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	custom_short_url = data.get('custom_short_url')
	expiration_date = data.get('expiration_date')

	if custom_short_url and custom_short_url in urls_db:
		return jsonify({'error': 'Custom short URL already exists'}), 400

	short_url = custom_short_url or ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	urls_db[short_url] = URL(original_url, short_url, datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S') if expiration_date else None)

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls_db.get(short_url)

	if not url:
		return jsonify({'error': 'URL not found'}), 404

	if url.expiration_date and url.expiration_date < datetime.now():
		return jsonify({'error': 'URL expired'}), 410

	return redirect(url.original_url, code=302)

if __name__ == '__main__':
	app.run(debug=True)
