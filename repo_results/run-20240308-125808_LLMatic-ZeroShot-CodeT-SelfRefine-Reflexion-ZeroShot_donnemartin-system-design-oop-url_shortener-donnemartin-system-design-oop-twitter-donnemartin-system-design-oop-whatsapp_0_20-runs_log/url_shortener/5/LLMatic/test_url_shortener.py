import pytest
from url_shortener import UrlShortener
import datetime

def test_url_shortener():
	url_shortener = UrlShortener()

	# Test URL validation
	assert url_shortener.validate_url('https://www.google.com') == True
	assert url_shortener.validate_url('invalid_url') == False

	# Test URL shortening
	original_url = 'https://www.google.com'
	short_url1 = url_shortener.generate_short_url(original_url)
	short_url2 = url_shortener.generate_short_url(original_url)
	assert len(short_url1) == 6
	assert len(short_url2) == 6
	assert short_url1 != short_url2

	# Test custom URL creation
	custom_url = 'custom'
	assert url_shortener.create_custom_short_url(custom_url, original_url) == custom_url
	assert url_shortener.create_custom_short_url(custom_url, original_url) == None

	# Test URL redirection
	assert url_shortener.redirect_to_original_url(short_url1) == original_url
	assert url_shortener.redirect_to_original_url(short_url2) == original_url
	assert url_shortener.redirect_to_original_url('invalid_short_url') == None

	# Test URL expiration
	expiration_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
	assert url_shortener.set_expiration(short_url1, expiration_date) == 'Expiration date set'

