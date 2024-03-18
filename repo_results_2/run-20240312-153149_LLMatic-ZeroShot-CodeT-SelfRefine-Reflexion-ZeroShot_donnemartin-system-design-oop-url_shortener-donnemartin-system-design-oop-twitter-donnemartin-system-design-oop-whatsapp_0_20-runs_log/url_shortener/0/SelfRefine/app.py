from flask import Flask, request, redirect
from dataclasses import dataclass
import requests
from geopy.geocoders import Nominatim
import datetime
import random
import string
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Mock database
DB = {}
USERS = {}

@dataclass
class URL:
	original: str
	shortened: str
	clicks: int
	click_data: list

@dataclass
class User:
	username: str
	password: str
	urls: list

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	
	# Check if username already exists
	if USERS.get(username):
		return {'error': 'Username already exists'}, 400
	
	# Create user and store in USERS
	user = User(username, generate_password_hash(password), [])
	USERS[username] = user
	
	return {'message': 'User created successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	
	# Check if user exists and password is correct
	user = USERS.get(username)
	if not user or not check_password_hash(user.password, password):
		return {'error': 'Invalid username or password'}, 400
	
	# Return user's URLs
	return {'urls': user.urls}, 200

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	username = data['username']
	original_url = data['url']
	custom_alias = data.get('alias')
	
	# Check if user is logged in
	user = USERS.get(username)
	if not user:
		return {'error': 'User not logged in'}, 401
	
	# Validate URL
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return {'error': 'Invalid URL'}, 400
	except:
		return {'error': 'Invalid URL'}, 400
	
	# Generate shortened URL
	shortened_url = custom_alias if custom_alias else ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	
	# Create URL object and store in DB
	url = URL(original_url, shortened_url, 0, [])
	DB[shortened_url] = url
	
	# Add URL to user's list
	user.urls.append(url)
	
	return {'shortened_url': shortened_url}, 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if not url:
		return {'error': 'URL not found'}, 404
	
	# Update click data
	url.clicks += 1
	geolocator = Nominatim(user_agent='url_shortener')
	location = geolocator.geocode(request.remote_addr)
	url.click_data.append({'time': datetime.datetime.now(), 'location': location})
	
	# Redirect to original URL
	return redirect(url.original, code=302)

if __name__ == '__main__':
	app.run(debug=True)
