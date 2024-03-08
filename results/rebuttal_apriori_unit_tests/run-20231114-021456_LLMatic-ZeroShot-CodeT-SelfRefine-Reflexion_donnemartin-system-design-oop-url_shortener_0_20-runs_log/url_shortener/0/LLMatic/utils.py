import string
import random
from urllib.parse import urlparse
from datetime import datetime
from models import URL, User

# Function to validate a URL
def validate_url(url):
	try:
		parsed = urlparse(url)
		return all([parsed.scheme, parsed.netloc])
	except ValueError:
		return False

# Function to generate a unique shortened URL
def generate_short_url(url, custom_slug=None, expiration_date=None):
	if not validate_url(url):
		return 'Invalid URL'
	if custom_slug:
		short_url = custom_slug
	else:
		short_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	user = User('test_user', 'password')
	new_url = URL(url, short_url, user, datetime.now(), expiration_date)
	user.add_url(new_url)
	User.save_to_db(user)
	URL.save_to_db(new_url)
	return short_url

# Function to get the original URL from the shortened URL
def get_original_url(short_url):
	url = URL.find_by_short_url(short_url)
	if url:
		return url.original_url
	return 'URL not found'

# Function to retrieve statistics about a shortened URL
def get_url_stats(short_url):
	url = URL.find_by_short_url(short_url)
	if url:
		clicks = url.clicks
		creation_date = url.creation_date
		expiration_date = url.expiration_date
		return {'clicks': clicks, 'creation_date': creation_date, 'expiration_date': expiration_date}
	return {'clicks': [], 'creation_date': None, 'expiration_date': None}

# Function to check whether a shortened URL has expired
def check_expiration(short_url):
	url = URL.find_by_short_url(short_url)
	if url and url.expiration_date:
		return datetime.now() > url.expiration_date
	return False
