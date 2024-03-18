from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import pytz
import uuid

app = Flask(__name__)

# Mock database
users = {}
urls = {}

@dataclass
class User:
	id: str
	urls: dict

@dataclass
class URL:
	original_url: str
	short_url: str
	user_id: str
	clicks: int
	click_details: list
	expiration_date: datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	user_id = str(uuid.uuid4())
	users[user_id] = User(user_id, {})
	return jsonify({'user_id': user_id}), 201

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	user_id = data.get('user_id')
	short_url = str(uuid.uuid4())[:8]
	expiration_date = data.get('expiration_date')
	if expiration_date:
		expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
	urls[short_url] = URL(original_url, short_url, user_id, 0, [], expiration_date)
	if user_id:
		users[user_id].urls[short_url] = urls[short_url]
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	url = urls.get(short_url)
	if not url or (url.expiration_date and url.expiration_date < datetime.now(pytz.UTC)):
		return jsonify({'error': 'URL not found or expired'}), 404
	url.clicks += 1
	url.click_details.append({'click_time': datetime.now(pytz.UTC).isoformat()})
	return redirect(url.original_url, code=302)

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	url = urls.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	return jsonify({'clicks': url.clicks, 'click_details': url.click_details}), 200

if __name__ == '__main__':
	app.run(debug=True)
