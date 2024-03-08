import string
import random
import requests
from database import add_url, record_click as db_record_click, get_analytics as db_get_analytics

# Function to generate a random string of a given length
def generate_random_string(length=8):
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Function to validate a URL
def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False

# Function to shorten a URL
def shorten_url(url):
	if validate_url(url):
		short_url = 'http://short.ly/' + generate_random_string()
		add_url(short_url, url)
		return short_url
	else:
		return None

# Function to record a click on a shortened URL
def record_click(short_url, geolocation):
	db_record_click(short_url, geolocation)

# Function to get the analytics for a shortened URL
def get_analytics(short_url):
	return db_get_analytics(short_url)
