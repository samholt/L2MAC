import url_shortener
from datetime import datetime, timedelta

# Test URL validation function
def test_validate_url():
	assert url_shortener.validate_url('https://www.google.com') == True
	assert url_shortener.validate_url('invalid_url') == False

# Test URL shortening function
def test_generate_short_url():
	short_url = url_shortener.generate_short_url('https://www.google.com')
	assert len(short_url) == 6
	assert url_shortener.DATABASE[short_url]['url'] == 'https://www.google.com'
	assert url_shortener.DATABASE[short_url]['expiration_time'] > datetime.now()

# Test custom short link function
def test_custom_short_link():
	custom_link = url_shortener.custom_short_link('https://www.google.com', 'google')
	assert custom_link == 'google'
	assert url_shortener.DATABASE[custom_link]['url'] == 'https://www.google.com'
	assert url_shortener.DATABASE[custom_link]['expiration_time'] > datetime.now()
	
	# Test that an error is returned if the custom link is already in use
	assert url_shortener.custom_short_link('https://www.google.com', 'google') == 'Custom link already in use'

# Test URL expiration
def test_url_expiration():
	expired_url = url_shortener.generate_short_url('https://www.google.com', expiration_minutes=-1)
	assert url_shortener.get_original_url(expired_url) == '404: URL not found or expired'

