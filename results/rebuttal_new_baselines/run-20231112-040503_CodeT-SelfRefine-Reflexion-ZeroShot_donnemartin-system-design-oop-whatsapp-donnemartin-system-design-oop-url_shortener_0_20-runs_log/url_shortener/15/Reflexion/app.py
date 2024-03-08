from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime
import pytz

app = Flask(__name__)

# Mock database
users = {}
urls = {}

@dataclass
class User:
	username: str
	password: str
	urls: dict

@dataclass
class Url:
	original_url: str
	short_url: str
	expiration_date: datetime
	clicks: int
	click_data: list

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	username = data.get('username')
	original_url = data.get('original_url')
	short_url = data.get('short_url')
	expiration_date = datetime.strptime(data.get('expiration_date'), '%Y-%m-%d %H:%M:%S')
	
	if username in users:
		user = users[username]
		user.urls[short_url] = Url(original_url, short_url, expiration_date, 0, [])
		urls[short_url] = user.urls[short_url]
		return {'message': 'URL shortened successfully'}, 200
	else:
		return {'message': 'User not found'}, 404

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url in urls:
		url = urls[short_url]
		if url.expiration_date > datetime.now(pytz.UTC):
			url.clicks += 1
			url.click_data.append({'click_time': datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')})
			return redirect(url.original_url, code=302)
		else:
			return {'message': 'URL expired'}, 410
	else:
		return {'message': 'URL not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
