import url_shortener
from datetime import datetime, timedelta

def test_generate_short_url():
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 6
	assert short_url.isalnum()

	custom_alias = 'custom'
	custom_short_url = url_shortener.generate_short_url(url, custom_alias)
	assert custom_short_url == custom_alias

	expired_short_url = url_shortener.generate_short_url(url, expiration=datetime.now() - timedelta(minutes=1))
	assert url_shortener.get_original_url(expired_short_url) is None

	unexpired_short_url = url_shortener.generate_short_url(url, expiration=datetime.now() + timedelta(minutes=1))
	assert url_shortener.get_original_url(unexpired_short_url) == url

def test_validate_url():
	valid_url = 'https://www.example.com'
	invalid_url = 'https://www.invalidurl.com'
	assert url_shortener.validate_url(valid_url) == True
	assert url_shortener.validate_url(invalid_url) == False

