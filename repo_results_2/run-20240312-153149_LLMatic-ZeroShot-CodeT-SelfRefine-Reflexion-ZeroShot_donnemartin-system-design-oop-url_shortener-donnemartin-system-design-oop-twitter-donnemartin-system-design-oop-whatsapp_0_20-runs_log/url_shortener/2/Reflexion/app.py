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
	short: str

@app.route('/', methods=['POST'])
def create_url():
	original_url = request.json['url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls_db[short_url] = original_url
	return {'short_url': short_url}, 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url in urls_db:
		return redirect(urls_db[short_url])
	else:
		return {'error': 'URL not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
