import url_shortener
from datetime import datetime, timedelta
import time

def test_generate_short_url():
	url1 = 'https://www.google.com'
	url2 = 'https://www.facebook.com'
	short_url1 = url_shortener.generate_short_url(url1)
	short_url2 = url_shortener.generate_short_url(url2)
	assert len(short_url1) == 6
	assert len(short_url2) == 6
	assert short_url1 != short_url2


def test_generate_custom_short_url():
	url = 'https://www.google.com'
	custom_short_url = 'GOOGL'
	short_url = url_shortener.generate_short_url(url, custom_short_url)
	assert short_url == custom_short_url


def test_validate_url():
	assert url_shortener.validate_url('https://www.google.com') == True
	assert url_shortener.validate_url('https://www.invalidurl.com') == False


def test_url_expiration():
	url = 'https://www.google.com'
	short_url = url_shortener.generate_short_url(url, expiration_date=datetime.now() + timedelta(seconds=1))
	assert url_shortener.get_url(short_url) == url
	time.sleep(2)
	assert url_shortener.get_url(short_url) == None
