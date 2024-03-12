import hashlib
import requests
from datetime import datetime, timedelta


def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False


def generate_short_url(url):
	url_hash = hashlib.md5(url.encode()).hexdigest()
	return url_hash[:6]


def handle_custom_short_link(custom_link, url_database):
	if custom_link in url_database:
		return False
	else:
		url_database[custom_link] = {'url': None, 'expiration': None}
		return True


def set_expiration(short_url, url_database, expiration_minutes):
	if short_url in url_database:
		expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)
		url_database[short_url]['expiration'] = expiration_time
		return True
	return False


def is_expired(short_url, url_database):
	if short_url in url_database:
		expiration_time = url_database[short_url]['expiration']
		if expiration_time is not None and datetime.now() > expiration_time:
			return True
	return False
