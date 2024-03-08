from flask import Flask, request, redirect
from dataclasses import dataclass
import random
import string

app = Flask(__name__)

# Mock database
urls_db = {}

@dataclass
class Url:
	original: str
	shortened: str
	clicks: int

@app.route('/shorten', methods=['POST'])
def shorten_url():
	original_url = request.json['url']
	shortened_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls_db[shortened_url] = Url(original=original_url, shortened=shortened_url, clicks=0)
	return {'shortened_url': shortened_url}

@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_original(shortened_url):
	if shortened_url in urls_db:
		urls_db[shortened_url].clicks += 1
		return redirect(urls_db[shortened_url].original)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/analytics/<shortened_url>', methods=['GET'])
def get_analytics(shortened_url):
	if shortened_url in urls_db:
		return {'original_url': urls_db[shortened_url].original, 'clicks': urls_db[shortened_url].clicks}
	else:
		return {'error': 'URL not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
