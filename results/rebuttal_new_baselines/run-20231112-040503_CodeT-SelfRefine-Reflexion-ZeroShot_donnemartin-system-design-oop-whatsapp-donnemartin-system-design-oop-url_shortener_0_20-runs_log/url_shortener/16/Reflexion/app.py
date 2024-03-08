from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import pytz

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class URL:
	original_url: str
	short_url: str
	user_id: str
	clicks: int
	expires_at: str

@dataclass
class User:
	user_id: str
	urls: list

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = URL(**data)
	urls[url.short_url] = url
	return jsonify(url), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url is None:
		return 'URL not found', 404
	
	# Parse the expires_at string into a datetime object
	expires_at = datetime.strptime(url.expires_at, '%Y-%m-%dT%H:%M:%S.%fZ')
	expires_at = expires_at.replace(tzinfo=pytz.UTC)
	
	# Check if the URL has expired
	if datetime.now(pytz.UTC) > expires_at:
		return 'URL has expired', 410
	
	url.clicks += 1
	return redirect(url.original_url, code=302)

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	url = urls.get(short_url)
	if url is None:
		return 'URL not found', 404
	return jsonify(url), 200

if __name__ == '__main__':
	app.run(debug=True)
