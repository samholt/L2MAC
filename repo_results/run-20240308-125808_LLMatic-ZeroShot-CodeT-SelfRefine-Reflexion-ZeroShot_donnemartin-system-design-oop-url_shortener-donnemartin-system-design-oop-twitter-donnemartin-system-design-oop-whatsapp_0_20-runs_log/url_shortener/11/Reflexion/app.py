from flask import Flask, request, redirect
import string
import random

app = Flask(__name__)

# Mock database
url_db = {}

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.json['url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url_db[short_url] = url
	return {'short_url': short_url}, 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = url_db[short_url]
	return redirect(url, code=302)

if __name__ == '__main__':
	app.run(debug=True)
