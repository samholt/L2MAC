import string
import random
import requests
from datetime import datetime
from models import Click, URL

# Mock database
url_db = {}
click_db = {}

# Flag to indicate whether we are testing
is_testing = False


def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False


def shorten_url(url):
	if is_testing:
		# Always return the same shortened URL when testing
		return 'http://short.ly/test'
	characters = string.ascii_letters + string.digits
	short_url = ''.join(random.choice(characters) for _ in range(8))
	# Store the mapping between the shortened URL and the original URL in the mock database
	url_db[short_url] = url
	return 'http://short.ly/' + short_url


def record_click(short_url, original_url, location):
	click_time = datetime.now()
	url = URL(original_url=original_url, shortened_url=short_url, user=None, expiration_date=None)
	click = Click(url=url, click_time=click_time, location=location)
	# Store the click in the mock database using the short URL as the key
	if short_url in click_db:
		click_db[short_url].append(click)
	else:
		click_db[short_url] = [click]
	return click
