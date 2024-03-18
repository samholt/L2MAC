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
	expiration = data.get('expiration')
	shortened_url = str(uuid.uuid4())[:8]
	DB[shortened_url] = URL(original_url, shortened_url, user, [], expiration)
	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = DB.get(short_url)
	if url and datetime.now() <= url.expiration:
		url.clicks.append((str(datetime.now()), request.remote_addr))
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

if __name__ == '__main__':
	app.run(debug=True)