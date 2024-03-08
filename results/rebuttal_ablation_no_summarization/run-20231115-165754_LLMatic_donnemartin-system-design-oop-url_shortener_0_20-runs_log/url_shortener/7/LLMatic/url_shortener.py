import hashlib
import requests
from datetime import datetime, timedelta

# Mock database
DATABASE = {}


def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False


def generate_short_url(url, expiry_days=30):
	short_url = hashlib.md5(url.encode()).hexdigest()[:10]
	while short_url in DATABASE:
		short_url = hashlib.md5((url + short_url).encode()).hexdigest()[:10]
	expiry_date = datetime.now() + timedelta(days=expiry_days)
	DATABASE[short_url] = {'url': url, 'expiry_date': expiry_date}
	return short_url


def handle_custom_short_link(url, custom_link, expiry_days=30):
	if custom_link in DATABASE:
		return None
	expiry_date = datetime.now() + timedelta(days=expiry_days)
	DATABASE[custom_link] = {'url': url, 'expiry_date': expiry_date}
	return custom_link
