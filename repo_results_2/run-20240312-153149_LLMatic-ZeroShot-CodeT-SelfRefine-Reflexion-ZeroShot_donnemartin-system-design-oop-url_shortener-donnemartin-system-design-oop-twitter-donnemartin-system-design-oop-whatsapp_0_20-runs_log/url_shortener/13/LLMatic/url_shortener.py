import string
import random
import requests
from datetime import datetime

# Mock database
url_database = {}


def generate_short_url(url, custom_short_url=None, expiration_date=None):
	if custom_short_url and custom_short_url not in url_database.values():
		short_url = custom_short_url
	else:
		short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
	url_database[short_url] = {'url': url, 'expiration_date': expiration_date}
	return short_url


def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False


def get_url(short_url):
	url_data = url_database.get(short_url)
	if url_data:
		if url_data['expiration_date'] and datetime.now() > url_data['expiration_date']:
			return None
		return url_data['url']
	return None
