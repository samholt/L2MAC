import string
import random
import requests
from datetime import datetime, timedelta

# Mock database
url_db = {}


def generate_short_url(length=6):
	# Function to generate a random short URL
	characters = string.ascii_letters + string.digits
	short_url = ''.join(random.choice(characters) for _ in range(length))
	url_db[short_url] = {'expiration': None}
	return short_url


def validate_url(url):
	# Function to validate a URL by sending a GET request
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return True
		else:
			return False
	except requests.exceptions.RequestException:
		return False


def set_url_expiration(short_url, expiration_minutes):
	# Function to set an expiration time for a short URL
	expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)
	url_db[short_url]['expiration'] = expiration_time


def check_url_expiration(short_url):
	# Function to check if a short URL has expired
	if datetime.now() > url_db[short_url]['expiration']:
		return True
	else:
		return False
