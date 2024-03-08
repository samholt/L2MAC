import string
import random
import requests


def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False


def generate_short_link(length=6):
	characters = string.ascii_letters + string.digits
	short_link = ''.join(random.choice(characters) for _ in range(length))
	return short_link


def handle_custom_short_link(requested_link, existing_links):
	if requested_link in existing_links:
		return {'error': 'Requested short link is already in use.'}
	else:
		return requested_link
