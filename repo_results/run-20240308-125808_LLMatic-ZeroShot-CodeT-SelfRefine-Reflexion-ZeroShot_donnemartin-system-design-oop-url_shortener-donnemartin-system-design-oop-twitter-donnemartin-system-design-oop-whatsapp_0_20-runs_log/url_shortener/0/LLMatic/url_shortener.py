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
def generate_short_url(url, expiration_minutes=0):
	if not validate_url(url):
		return 'Invalid URL'
	
	# Generate a unique string of characters
	short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	
	# Check if the short url already exists in the database
	while short_url in DATABASE:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	
	DATABASE[short_url] = url
	
	if expiration_minutes > 0:
		EXPIRATION[short_url] = datetime.now() + timedelta(minutes=expiration_minutes)
	
	return short_url


# Function to handle custom short links
def custom_short_link(url, custom_link, expiration_minutes=0):
	if not validate_url(url):
		return 'Invalid URL'
	
	# Check if the custom link is already in use
	if custom_link in DATABASE:
		return 'Custom link already in use'
	
	DATABASE[custom_link] = url
	
	if expiration_minutes > 0:
		EXPIRATION[custom_link] = datetime.now() + timedelta(minutes=expiration_minutes)
	
	return custom_link

# Function to get the original URL from the shortened URL
def get_original_url(short_url):
	if short_url in EXPIRATION and datetime.now() > EXPIRATION[short_url]:
		del DATABASE[short_url]
		del EXPIRATION[short_url]
		return None
	return DATABASE.get(short_url)
