import string
import random
import requests

# Mock database
DATABASE = {}


def generate_short_url(length=6):
	characters = string.ascii_letters + string.digits
	short_url = ''.join(random.choice(characters) for _ in range(length))
	while short_url in DATABASE:
		short_url = ''.join(random.choice(characters) for _ in range(length))
	return short_url


def check_url_availability(url):
	if url in DATABASE:
		return False
	return True


def check_url_validity(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False


def shorten_url(original_url, custom_short_url=None):
	if not check_url_validity(original_url):
		return 'Invalid URL'
	if custom_short_url:
		if not check_url_availability(custom_short_url):
			return 'Custom short URL is not available'
		DATABASE[custom_short_url] = original_url
		return custom_short_url
	short_url = generate_short_url()
	DATABASE[short_url] = original_url
	return short_url
