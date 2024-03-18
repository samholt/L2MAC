from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import dateutil.parser
import random
import string

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original: str
	shortened: str
	expiration: datetime
	clicks: int

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['url']
	expiration_date = dateutil.parser.parse(data['expiration'])
	shortened_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	DB[shortened_url] = URL(original_url, shortened_url, expiration_date, 0)
	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = DB.get(short_url)
	if url and url.expiration > datetime.now():
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return 'URL not found or expired', 404

if __name__ == '__main__':
	app.run(debug=True)
