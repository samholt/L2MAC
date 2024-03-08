import url_shortener
from datetime import datetime, timedelta


def test_generate_short_url():
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 10
	assert short_url.isalnum()

	# Test uniqueness of the shortened URL
	new_url = 'https://www.different.com'
	new_short_url = url_shortener.generate_short_url(new_url)
	assert new_short_url != short_url


def test_validate_url():
	# Test with a valid URL
	valid_url = 'https://www.example.com'
	assert url_shortener.validate_url(valid_url) is True

	# Test with an invalid URL
	invalid_url = 'https://www.invalid.com'
	assert url_shortener.validate_url(invalid_url) is False


def test_store_and_get_url():
	# Mock a Flask application
	class MockApp:
		def __init__(self):
			self.url_db = {}

	app = MockApp()
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	url_shortener.store_url(app, short_url, url, 1)

	# Test that the URL can be retrieved before it expires
	assert url_shortener.get_url(app, short_url) == url

	# Test that the URL cannot be retrieved after it expires
	url_shortener.store_url(app, short_url, url, -1)
	assert url_shortener.get_url(app, short_url) is None
