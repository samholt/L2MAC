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
	user_id = data.get('user_id')
	short_url = data.get('short_url', str(uuid.uuid4())[:8])
	expiration_date = data.get('expiration_date')
	
	if not original_url or not user_id:
		return jsonify({'error': 'Missing required fields'}), 400
	
	new_url = URL(original_url, short_url, user_id, 0, [], expiration_date)
	DB[short_url] = new_url
	
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	
	url.clicks += 1
	url.click_data.append({'click_time': datetime.now()})
	
	return redirect(url.original_url, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	user_id = request.args.get('user_id')
	
	if not user_id:
		return jsonify({'error': 'Missing user_id'}), 400
	
	user_urls = [url for url in DB.values() if url.user_id == user_id]
	
	return jsonify({'urls': user_urls}), 200

if __name__ == '__main__':
	app.run(debug=True)
