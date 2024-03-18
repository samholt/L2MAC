import pytest
import services

def test_generate_short_url():
	short_url1 = services.generate_short_url()
	short_url2 = services.generate_short_url()
	assert len(short_url1) == 6
	assert len(short_url2) == 6
	assert short_url1 != short_url2

def test_validate_url():
	assert services.validate_url('https://www.google.com')
	assert not services.validate_url('invalid_url')

def test_create_short_url():
	original_url = 'http://example.com'
	short_url = services.create_short_url('test_user', original_url)
	assert len(short_url) == 6
	assert services.get_original_url(short_url) == original_url

def test_get_original_url():
	assert services.get_original_url('nonexistent') is None
