import pytest
from admin import Admin
from user import users


def test_admin():
	admin = Admin('admin', 'admin')
	admin.create_account()

	user1 = users['admin']
	user1.add_url('https://google.com', 'goo.gl')
	user2 = users['admin']
	user2.add_url('https://facebook.com', 'fb.com')

	assert admin.view_all_urls() == {'goo.gl': 'https://google.com', 'fb.com': 'https://facebook.com'}

	admin.delete_url('goo.gl')
	assert admin.view_all_urls() == {'fb.com': 'https://facebook.com'}

	admin.delete_user('admin')
	assert 'admin' not in users

	assert isinstance(admin.view_system_analytics(), dict)
