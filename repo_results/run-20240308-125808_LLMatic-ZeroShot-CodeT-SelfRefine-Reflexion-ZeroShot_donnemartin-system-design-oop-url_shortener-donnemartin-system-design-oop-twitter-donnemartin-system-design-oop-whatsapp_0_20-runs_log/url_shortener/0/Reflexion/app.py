from flask import Flask, request, redirect
from dataclasses import dataclass
import random
import string

app = Flask(__name__)

# Mock database
urls_db = {}

@dataclass
class URL:
	long_url: str
	short_url: str = ''

	def generate_short_url(self):
		letters = string.ascii_lowercase
		while True:
			short_url = ''.join(random.choice(letters) for i in range(5))
			if short_url not in urls_db:
				self.short_url = short_url
				break

@app.route('/', methods=['POST'])
def create_short_url():
	url_data = request.get_json()
	url = URL(url_data['long_url'])
	url.generate_short_url()
	urls_db[url.short_url] = url.long_url
	return {'short_url': url.short_url}, 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
	long_url = urls_db.get(short_url)
	if long_url is None:
		return {'error': 'URL not found'}, 404
	return redirect(long_url, code=302)

if __name__ == '__main__':
	app.run(debug=True)
