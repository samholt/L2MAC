from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime
import string
import random

app = Flask(__name__)

# Mock database
urls_db = {}

@dataclass
class URL:
	original_url: str
	short_url: str
	expiration_date: datetime

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	original_url = request.json['original_url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	expiration_date = request.json.get('expiration_date')
	if expiration_date:
		expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
	urls_db[short_url] = URL(original_url, short_url, expiration_date)
	return {'short_url': short_url}, 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls_db.get(short_url)
	if url and (not url.expiration_date or url.expiration_date > datetime.now()):
		return redirect(url.original_url)
	else:
		return 'URL not found or expired', 404

if __name__ == '__main__':
	app.run(debug=True)
