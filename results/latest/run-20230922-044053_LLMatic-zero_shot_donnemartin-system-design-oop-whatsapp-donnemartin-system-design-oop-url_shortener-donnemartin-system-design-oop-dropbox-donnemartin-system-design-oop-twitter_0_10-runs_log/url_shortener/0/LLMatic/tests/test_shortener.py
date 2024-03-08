from url_shortener.models import User
from url_shortener.shortener import create_shortened_url
from datetime import datetime, timedelta


def test_shorten_url():
	user = User('test_user', 'password')
	original_url = 'http://example.com'
	shortened_url = create_shortened_url(original_url, user)
	assert shortened_url.original_url == original_url
	assert shortened_url.shortened_url != original_url
	assert shortened_url.user == user
	assert shortened_url.expires_at == datetime.now() + timedelta(days=30)
