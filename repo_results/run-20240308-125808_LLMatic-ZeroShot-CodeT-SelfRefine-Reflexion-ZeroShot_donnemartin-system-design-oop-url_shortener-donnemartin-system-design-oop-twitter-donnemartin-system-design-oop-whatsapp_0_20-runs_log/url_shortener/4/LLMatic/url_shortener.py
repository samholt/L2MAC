import string
import random
import requests
from datetime import datetime, timedelta

# Mock database
DATABASE = {}

# URL validation function
def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False

# URL shortening function
def generate_short_url(url, expiration_minutes=15):
	if not validate_url(url):
		return 'Invalid URL'
	
	# Generate a unique string of 6 characters
	short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	
	# Check if the short URL is already in use
	while short_url in DATABASE:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	
	expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)
	DATABASE[short_url] = {'url': url, 'expiration_time': expiration_time}
	
	return short_url

# Custom short link function
def custom_short_link(url, custom_link, expiration_minutes=15):
	if not validate_url(url):
		return 'Invalid URL'
	
	if custom_link in DATABASE:
		return 'Custom link already in use'
	
	expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)
	DATABASE[custom_link] = {'url': url, 'expiration_time': expiration_time}
	
	return custom_link

# Function to get original URL from the database
def get_original_url(short_url):
	url_data = DATABASE.get(short_url)
	if url_data and url_data['expiration_time'] > datetime.now():
		return url_data['url']
	return '404: URL not found or expired'

