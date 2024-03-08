import pytest
from views import redirect
from models import URL
from database import DATABASE
from datetime import datetime, timedelta

# Helper function to create a URL with a specified expiration time
def create_url_with_expiration(expiration_time):
	url = URL('https://example.com', 'short_url', None, expiration_time)
	DATABASE[url.short_url] = url
	return url

# Test that a URL with an expiration time in the future does not expire
def test_future_expiration():
	future_expiration_time = datetime.now() + timedelta(minutes=10)
	url = create_url_with_expiration(future_expiration_time)
	assert redirect(url.short_url) == url.original_url

# Test that a URL with an expiration time in the past expires
def test_past_expiration():
	past_expiration_time = datetime.now() - timedelta(minutes=10)
	url = create_url_with_expiration(past_expiration_time)
	assert redirect(url.short_url) == 'URL expired'

# Test that a URL without an expiration time does not expire
def test_no_expiration():
	url = create_url_with_expiration(None)
	assert redirect(url.short_url) == url.original_url
