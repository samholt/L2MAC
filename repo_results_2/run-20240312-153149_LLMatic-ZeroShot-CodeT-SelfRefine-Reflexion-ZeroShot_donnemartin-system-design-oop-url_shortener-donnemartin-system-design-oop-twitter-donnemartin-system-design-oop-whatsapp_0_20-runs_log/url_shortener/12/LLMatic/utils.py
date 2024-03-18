import string
import random
from urllib.parse import urlparse


def validate_url(url):
	try:
		parsed_url = urlparse(url)
		return all([parsed_url.scheme, parsed_url.netloc])
	except ValueError:
		return False


def generate_short_link(length=6):
	characters = string.ascii_letters + string.digits
	short_link = ''.join(random.choice(characters) for _ in range(length))
	return short_link


def check_availability(short_link, url_db):
	return short_link not in url_db
