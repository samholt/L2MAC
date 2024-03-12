import string
import random
from urllib.parse import urlparse


def validate_url(url):
	try:
		parsed = urlparse(url)
		return all([parsed.scheme, parsed.netloc])
	except ValueError:
		return False


def generate_short_link(length=6):
	characters = string.ascii_letters + string.digits
	short_link = ''.join(random.choice(characters) for _ in range(length))
	return short_link
