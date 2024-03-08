from flask import Flask, request, redirect, jsonify
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

@app.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	url = DB.get(shortened_url)
	if url and url.expiration > datetime.now():
		url.clicks.append(datetime.now())
		return redirect(url.original, code=302)
	else:
		return 'URL not found or expired', 404

if __name__ == '__main__':
	app.run(debug=True)
