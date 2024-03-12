import string
import random
import requests
from datetime import datetime


url_db = {}


def generate_short_url(url, custom_alias=None, expiration=None):
	if custom_alias:
		short_url = custom_alias
	else:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	url_db[short_url] = {'url': url, 'expiration': expiration}
	return short_url


def get_original_url(short_url):
	url_data = url_db.get(short_url)
	if url_data and (url_data['expiration'] is None or url_data['expiration'] > datetime.now()):
		return url_data['url']


def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False

