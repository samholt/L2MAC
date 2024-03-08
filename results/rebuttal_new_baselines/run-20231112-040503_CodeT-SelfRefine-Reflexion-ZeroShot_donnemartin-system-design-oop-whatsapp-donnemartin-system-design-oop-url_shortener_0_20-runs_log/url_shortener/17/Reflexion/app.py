from flask import Flask, request, redirect
from dataclasses import dataclass
import random
import string

app = Flask(__name__)

urls_db = {}

@dataclass
class URL:
	long_url: str
	short_url: str
	clicks: int

@app.route('/shorten', methods=['POST'])
def shorten_url():
	long_url = request.json['long_url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls_db[short_url] = URL(long_url, short_url, 0)
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url in urls_db:
		urls_db[short_url].clicks += 1
		return redirect(urls_db[short_url].long_url, code=302)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	if short_url in urls_db:
		return {'clicks': urls_db[short_url].clicks}
	else:
		return {'error': 'URL not found'}, 404
