import pytest
from services.url_shortener import URLShortener


def test_shorten_url():
	url_shortener = URLShortener()
	short_url = url_shortener.shorten('https://www.google.com')
	assert len(short_url) == 6
	assert url_shortener.get_url(short_url) == 'https://www.google.com'

	custom_url = url_shortener.shorten('https://www.google.com', 'google')
	assert custom_url == 'google'
	assert url_shortener.get_url('google') == 'https://www.google.com'

	invalid_url = url_shortener.shorten('invalid_url')
	assert invalid_url == 'Invalid URL'

	used_alias = url_shortener.shorten('https://www.google.com', 'google')
	assert used_alias == 'Alias already in use'
