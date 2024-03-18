from flask import Flask, request, redirect
from dataclasses import dataclass
import random
import string
import datetime
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original: str
	short: str
	clicks: int
	click_data: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	original_url = request.json['url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	DB[short_url] = URL(original_url, short_url, 0, [])
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	if short_url in DB:
		DB[short_url].clicks += 1
		DB[short_url].click_data.append({'time': datetime.datetime.now(), 'location': get_location()})
		return redirect(DB[short_url].original, code=302)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	if short_url in DB:
		return {'original_url': DB[short_url].original, 'clicks': DB[short_url].clicks, 'click_data': DB[short_url].click_data}
	else:
		return {'error': 'URL not found'}, 404

# Mock function to get location
def get_location():
	geolocator = Nominatim(user_agent='url_shortener')
	location = geolocator.geocode('127.0.0.1')
	return location.address if location else 'Unknown location'

if __name__ == '__main__':
	app.run(debug=True)
