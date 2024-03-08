from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import pytz

app = Flask(__name__)

urls_db = {}
users_db = {}

@dataclass
class URL:
	original_url: str
	short_url: str
	user_id: str
	clicks: int
	created_at: datetime
	expires_at: datetime or None

@dataclass
class User:
	user_id: str
	urls: list

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	short_url = data['short_url']
	user_id = data['user_id']
	expires_at = data.get('expires_at')
	if expires_at:
		expires_at = datetime.strptime(expires_at, '%Y-%m-%dT%H:%M:%S.%fZ')
		expires_at = expires_at.replace(tzinfo=pytz.UTC)
	url = URL(original_url, short_url, user_id, 0, datetime.now(pytz.UTC), expires_at)
	urls_db[short_url] = url
	if user_id in users_db:
		users_db[user_id].urls.append(url)
	else:
		users_db[user_id] = User(user_id, [url])
	return jsonify({'message': 'URL shortened successfully'}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	url = urls_db.get(short_url)
	if url and (not url.expires_at or url.expires_at > datetime.now(pytz.UTC)):
		url.clicks += 1
		return redirect(url.original_url, code=302)
	else:
		return jsonify({'message': 'URL not found or expired'}), 404

if __name__ == '__main__':
	app.run(debug=True)
