import pytest
from utils import validate_url, generate_short_url, get_original_url, get_url_stats, check_expiration
from models import URL, User
from datetime import datetime, timedelta

# Test that the validate_url function correctly validates URLs
def test_validate_url():
	assert validate_url('https://example.com') is True
	assert validate_url('invalid') is False

# Test that the generate_short_url function correctly generates shortened URLs
def test_generate_short_url():
	short_url = generate_short_url('https://example.com')
	assert len(short_url) < len('https://example.com')

# Test that the get_original_url function correctly retrieves the original URL from a shortened URL
def test_get_original_url():
	short_url = generate_short_url('https://example.com')
	assert get_original_url(short_url) == 'https://example.com'

# Test that the get_url_stats function correctly retrieves statistics about a shortened URL
def test_get_url_stats():
	short_url = generate_short_url('https://example.com')
	stats = get_url_stats(short_url)
	assert stats['clicks'] == 0
	assert 'creation_date' in stats
	assert 'expiration_date' in stats

# Test that the check_expiration function correctly checks whether a shortened URL has expired
def test_check_expiration():
	short_url = generate_short_url('https://example.com')
	assert check_expiration(short_url) is False
	short_url = generate_short_url('https://example.com', expiration_date=datetime.now() - timedelta(minutes=1))
	assert check_expiration(short_url) is True
