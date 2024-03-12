import string
import random
import requests
from datetime import datetime, timedelta


# Mock database
DATABASE = {}
EXPIRATION_TIMES = {}


# Function to validate URLs
def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False


# Function to generate unique shortened URLs
def generate_short_url(url):
	if url in DATABASE:
		return DATABASE[url]
	else:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
		while short_url in DATABASE.values():
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
		DATABASE[url] = short_url
		EXPIRATION_TIMES[short_url] = datetime.now() + timedelta(days=365)  # default expiration time is 1 year
		return short_url


# Function to handle custom short links
def custom_short_link(url, custom_link):
	if custom_link in DATABASE.values():
		return 'Error: Custom link already in use'
	else:
		DATABASE[url] = custom_link
		EXPIRATION_TIMES[custom_link] = datetime.now() + timedelta(days=365)  # default expiration time is 1 year
		return custom_link


# Function to get original URL from short URL
def get_original_url(short_url):
	if datetime.now() > EXPIRATION_TIMES[short_url]:
		return 'Error: This link has expired'
	for url, s_url in DATABASE.items():
		if s_url == short_url:
			return url
	return None


# Function to set expiration time for a URL
def set_expiration_time(short_url, days):
	EXPIRATION_TIMES[short_url] = datetime.now() + timedelta(days=days)
	return EXPIRATION_TIMES[short_url]

