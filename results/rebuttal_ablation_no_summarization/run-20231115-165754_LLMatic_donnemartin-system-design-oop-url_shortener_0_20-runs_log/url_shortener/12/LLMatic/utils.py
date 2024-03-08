import string
import random
import requests
from datetime import datetime

# This file will contain utility functions

# Function to generate a unique shortened URL

def generate_short_url(url):
	# Generate a random string of fixed length
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
	return short_url

# Function to validate that a given URL is active and legitimate
def validate_url(url):
	try:
		response = requests.get(url)
		# If the response was successful, no Exception will be raised
		response.raise_for_status()
	except requests.exceptions.RequestException as err:
		print(f'Error occurred: {err}')
		return False
	else:
		print('URL is valid and active.')
		return True

# Function to record a click event
def record_click(url_id, location, click_db):
	if url_id in click_db:
		click_db[url_id].append({'timestamp': datetime.now().isoformat(), 'location': location})
	else:
		click_db[url_id] = [{'timestamp': datetime.now().isoformat(), 'location': location}]
	return click_db

# Function to check if a URL has expired
def has_url_expired(url):
	if url.expiration_date is None:
		return False
	return datetime.now() > datetime.fromisoformat(url.expiration_date)
