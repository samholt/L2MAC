import pytest
from models import User, URL, Click
from database import DATABASE


def test_user_methods():
	user = User('testuser', 'password')
	DATABASE['testuser'] = user
	url = URL('https://example.com', 'short_url', user, None)
	user.urls['short_url'] = url
	assert user.get_shortened_urls() == ['short_url']
	user.edit_url('short_url', 'new_short_url')
	assert 'new_short_url' in user.get_shortened_urls()
	user.delete_url('new_short_url')
	assert 'new_short_url' not in user.get_shortened_urls()

