import pytest
from user import User, users


def test_user():
	user = User('test_user', 'password')
	user.create_account()
	assert user in users.values()

	user.add_url('https://www.google.com', 'goo.gl')
	assert 'goo.gl' in user.view_urls()

	user.edit_url('goo.gl', 'https://www.yahoo.com')
	assert user.view_urls()['goo.gl'] == 'https://www.yahoo.com'

	user.delete_url('goo.gl')
	assert 'goo.gl' not in user.view_urls()

	user.add_url('https://www.google.com', 'goo.gl')
	user.view_analytics()
	assert 'goo.gl' in user.view_analytics()
