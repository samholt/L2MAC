import pytest
from user import User

def test_user():
	user = User('test_user')
	user.create_url('https://www.google.com', 'goog')
	assert user.get_urls() == {'goog': {'original_url': 'https://www.google.com', 'clicks': 0, 'clicks_data': []}}
	user.edit_url('goog', 'https://www.yahoo.com')
	assert user.get_urls() == {'goog': {'original_url': 'https://www.yahoo.com', 'clicks': 0, 'clicks_data': []}}
	user.delete_url('goog')
	assert user.get_urls() == {}
	user.create_url('https://www.google.com', 'goog')
	assert user.get_url_analytics('goog') == (0, [])
