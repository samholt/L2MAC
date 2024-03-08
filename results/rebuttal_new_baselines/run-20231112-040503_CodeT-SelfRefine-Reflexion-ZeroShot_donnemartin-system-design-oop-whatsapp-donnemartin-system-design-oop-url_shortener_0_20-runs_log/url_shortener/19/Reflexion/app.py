from flask import Flask, request, redirect
from dataclasses import dataclass
import random
import string

app = Flask(__name__)

# Mock database
urls_db = {}

@dataclass
class Url:
	long_url: str
	short_url: str

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	long_url = request.json['long_url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls_db[short_url] = long_url
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
	long_url = urls_db.get(short_url)
	if long_url is not None:
		return redirect(long_url)
	else:
		return {'error': 'URL not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
