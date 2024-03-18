import random
import string
import re
from models import URL

url_db = {}

def generate_short_url():
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def validate_url(url):
	regex = re.compile(
		'^(?:http|ftp)s?://' # http:// or https://
		'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\\.)+(?:[A-Z]{2,6}\\.?|[A-Z0-9-]{2,}\\.?)|' #domain...
		'localhost|' #localhost...
		'\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})' # ...or ip
		'(?::\\d+)?' # optional port
		'(?:/?|[/?]\\S+)?$', re.IGNORECASE)
	return re.match(regex, url) is not None

def create_short_url(user, original_url):
	short_url = generate_short_url()
	url_db[short_url] = URL(original_url, short_url, user)
	return short_url

def get_original_url(short_url):
	url = url_db.get(short_url)
	if url is not None:
		return url.original_url
	else:
		return None
