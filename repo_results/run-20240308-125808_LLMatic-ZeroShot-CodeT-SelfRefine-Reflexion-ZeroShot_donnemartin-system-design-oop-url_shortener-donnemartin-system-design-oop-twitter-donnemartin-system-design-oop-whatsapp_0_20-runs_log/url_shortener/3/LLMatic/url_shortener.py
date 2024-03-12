import string
import random
from urllib.parse import urlparse
from datetime import datetime, timedelta

# Mock database
url_db = {}


def validate_url(url):
	try:
		result = urlparse(url)
		return all([result.scheme, result.netloc])
	except ValueError:
		return False


def generate_short_link(length=6):
	characters = string.ascii_letters + string.digits
	short_link = ''.join(random.choice(characters) for _ in range(length))
	return short_link


def handle_custom_link(custom_link):
	return custom_link if custom_link else generate_short_link()


def set_expiration(short_link, expiration_time=None):
	if expiration_time:
		expiration_date = datetime.now() + timedelta(minutes=expiration_time)
	else:
		expiration_date = None
	url_db[short_link] = {'expiration_date': expiration_date}


def get_short_link(short_link):
	url_data = url_db.get(short_link)
	if url_data and (not url_data['expiration_date'] or datetime.now() < url_data['expiration_date']):
		return short_link
	else:
		return 'This URL has expired.'
