import pytest
from admin import Admin
from user import User
from analytics import Analytics


def test_admin():
	admin = Admin('admin')
	user1 = User('user1')
	user2 = User('user2')
	analytics = Analytics()

	admin.add_user(user1)
	admin.add_user(user2)

	user1.add_url('abc', 'https://abc.com')
	user2.add_url('xyz', 'https://xyz.com')

	assert admin.view_all_urls() == {'abc': 'https://abc.com', 'xyz': 'https://xyz.com'}

	admin.delete_url('abc')
	assert admin.view_all_urls() == {'xyz': 'https://xyz.com'}

	admin.delete_user('user1')
	assert 'user1' not in admin.all_users

	assert admin.monitor_system(analytics) == {'xyz': []}
