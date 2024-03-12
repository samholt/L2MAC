import url_shortener


def test_generate_short_url():
	"""Test the generate_short_url function."""
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 10
	assert isinstance(short_url, str)

	# Test custom short URL
	custom_short_url = 'custom'
	short_url = url_shortener.generate_short_url(url, custom_short_url)
	assert short_url == custom_short_url

	# Test custom short URL already in use
	short_url = url_shortener.generate_short_url(url, custom_short_url)
	assert short_url != custom_short_url


def test_validate_url():
	"""Test the validate_url function."""
	valid_url = 'https://www.example.com'
	invalid_url = 'https://www.invalidurl.com'
	assert url_shortener.validate_url(valid_url) is True
	assert url_shortener.validate_url(invalid_url) is False
