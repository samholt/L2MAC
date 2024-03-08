import pytest
from utils import validate_url, shorten_url

# Test the URL validation function
@pytest.mark.parametrize('url, expected', [
	('http://google.com', True),
	('http://thisurldoesnotexist.com', True),
	('not a url', False)
])
def test_validate_url(url, expected):
	assert validate_url(url) == expected

# Test the URL shortening function
@pytest.mark.parametrize('url', [
	'http://google.com',
	'http://github.com'
])
def test_shorten_url(url):
	short_url = shorten_url(url)
	assert short_url is not None
	assert 'http://short.ly/' in short_url
