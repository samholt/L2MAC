import pytest
from admin import Admin
from user import User
from shortener import Shortener

def test_admin():
	system = Shortener()
	admin = Admin('admin', system)
	user1 = User('user1')
	user2 = User('user2')
	system.users = {'admin': admin, 'user1': user1, 'user2': user2}

	user1.create_url('https://example.com', 'exmpl')
	user2.create_url('https://google.com', 'ggl')

	assert admin.view_all_urls() == {'exmpl': {'original_url': 'https://example.com', 'clicks': 0, 'clicks_data': []}, 'ggl': {'original_url': 'https://google.com', 'clicks': 0, 'clicks_data': []}}

	admin.delete_url('user1', 'exmpl')
	assert admin.view_all_urls() == {'ggl': {'original_url': 'https://google.com', 'clicks': 0, 'clicks_data': []}}

	admin.delete_user('user2')
	assert admin.view_all_urls() == {}

	assert admin.monitor_system() == {'total_users': 2, 'total_urls': 0}
