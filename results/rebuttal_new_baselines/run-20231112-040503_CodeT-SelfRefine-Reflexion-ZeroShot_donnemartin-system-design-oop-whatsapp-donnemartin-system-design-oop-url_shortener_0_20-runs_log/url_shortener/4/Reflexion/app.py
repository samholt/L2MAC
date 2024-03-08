from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import pytz
import uuid

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class URL:
	original_url: str
	short_url: str
	creation_time: datetime
	expiration_time: datetime
	clicks: int
	click_details: list

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	short_url = str(uuid.uuid4())[:8]
	creation_time = datetime.now(pytz.utc)
	expiration_time = creation_time + timedelta(days=30)
	clicks = 0
	click_details = []
	url = URL(original_url, short_url, creation_time, expiration_time, clicks, click_details)
	DATABASE[short_url] = url
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DATABASE.get(short_url)
	if url and url.expiration_time > datetime.now(pytz.utc):
		url.clicks += 1
		url.click_details.append({'click_time': datetime.now(pytz.utc)})
		return redirect(url.original_url, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

if __name__ == '__main__':
	app.run(debug=True)
