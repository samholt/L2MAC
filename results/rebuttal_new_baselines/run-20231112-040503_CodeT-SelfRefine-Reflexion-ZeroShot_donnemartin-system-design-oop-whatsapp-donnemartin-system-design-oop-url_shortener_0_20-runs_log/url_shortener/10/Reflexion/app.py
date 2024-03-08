from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import random
import string

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class URL:
	original: str
	short: str
	user: str
	expires_at: datetime

@dataclass
class User:
	username: str
	password: str
	urls: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user = data.get('user')
	expires_at = datetime.strptime(data.get('expires_at'), '%Y-%m-%d %H:%M:%S')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls[short_url] = URL(original_url, short_url, user, expires_at)
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url and url.expires_at > datetime.now():
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

if __name__ == '__main__':
	app.run(debug=True)
