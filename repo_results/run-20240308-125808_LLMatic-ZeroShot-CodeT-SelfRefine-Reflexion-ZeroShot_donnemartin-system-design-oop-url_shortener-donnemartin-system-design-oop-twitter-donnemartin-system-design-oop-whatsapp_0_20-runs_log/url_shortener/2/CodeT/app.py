from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original_url: str
	short_url: str
	user_id: str
	clicks: int
	click_data: list
	expiration_date: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	short_url = data.get('short_url', str(uuid.uuid4())[:8])
	user_id = data.get('user_id')
	expiration_date = data.get('expiration_date')
	url = URL(original_url, short_url, user_id, 0, [], expiration_date)
	DB[short_url] = url
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = DB.get(short_url)
	if url and (not url.expiration_date or url.expiration_date > datetime.now()):
		url.clicks += 1
		url.click_data.append({'click_time': datetime.now().isoformat()})
		return redirect(url.original_url, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	url = DB.get(short_url)
	if url:
		return jsonify({'clicks': url.clicks, 'click_data': url.click_data}), 200
	else:
		return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
