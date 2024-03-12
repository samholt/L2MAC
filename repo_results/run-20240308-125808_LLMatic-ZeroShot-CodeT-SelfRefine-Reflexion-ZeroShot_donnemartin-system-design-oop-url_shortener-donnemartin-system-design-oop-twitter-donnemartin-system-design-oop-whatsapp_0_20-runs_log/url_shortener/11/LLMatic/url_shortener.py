import string
import random
import requests
from datetime import datetime, timedelta


# Mock database
DATABASE = {}
EXPIRATION = {}


# Function to validate the URL
def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False


# Function to generate a unique shortened URL
def generate_short_url(url):
	if url in DATABASE:
		return DATABASE[url]
	else:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
		DATABASE[url] = short_url
		return short_url


# Function to handle custom short links
def custom_short_link(url, custom_link):
	if custom_link in DATABASE.values():
		return 'Link already in use'
	else:
		DATABASE[url] = custom_link
		return custom_link

# Function to set expiration date/time for the shortened URL
def set_expiration(short_url, expiration_time):
	if short_url in DATABASE.values():
		EXPIRATION[short_url] = datetime.now() + timedelta(minutes=expiration_time)
		return 'Expiration time set'
	else:
		return 'Short URL not found'

