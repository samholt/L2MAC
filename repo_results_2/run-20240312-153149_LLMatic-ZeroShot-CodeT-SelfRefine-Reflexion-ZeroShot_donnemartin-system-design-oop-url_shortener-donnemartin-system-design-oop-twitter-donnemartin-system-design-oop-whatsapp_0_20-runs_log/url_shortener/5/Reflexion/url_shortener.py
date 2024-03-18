from flask import Flask, request, redirect
from dataclasses import dataclass
import random
import string

app = Flask(__name__)

# Mock database
urls_db = {}

@dataclass
class URL:
	original: str
	short: str
	clicks: int

@app.route('/shorten', methods=['POST'])
def shorten_url():
	original_url = request.json['url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls_db[short_url] = URL(original=original_url, short=short_url, clicks=0)
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	if short_url in urls_db:
		urls_db[short_url].clicks += 1
		return redirect(urls_db[short_url].original)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	if short_url in urls_db:
		return {'original_url': urls_db[short_url].original, 'clicks': urls_db[short_url].clicks}
	else:
		return {'error': 'URL not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
