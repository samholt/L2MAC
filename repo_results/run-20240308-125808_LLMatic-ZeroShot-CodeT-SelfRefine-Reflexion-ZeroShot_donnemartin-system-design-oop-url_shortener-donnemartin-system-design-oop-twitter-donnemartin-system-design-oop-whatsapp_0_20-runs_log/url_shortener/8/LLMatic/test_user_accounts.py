import pytest
from user_accounts import UserAccount

def test_user_account():
	user = UserAccount('test_user')
	assert user.username == 'test_user'
	assert user.view_urls() == {}

	user.create_url('https://www.google.com', 'goog')
	assert user.view_urls() == {'goog': 'https://www.google.com'}

	user.edit_url('goog', 'https://www.gmail.com')
	assert user.view_urls() == {'goog': 'https://www.gmail.com'}

	user.delete_url('goog')
	assert user.view_urls() == {}

	user.create_url('https://www.google.com', 'goog')
	user.create_url('https://www.facebook.com', 'fb')
	analytics = {'goog': {'clicks': 5, 'dates': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'], 'ips': ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']}, 'fb': {'clicks': 3, 'dates': ['2022-01-01', '2022-01-02', '2022-01-03'], 'ips': ['192.168.1.1', '192.168.1.2', '192.168.1.3']}}
	assert user.view_analytics(analytics) == {'goog': {'clicks': 5, 'dates': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'], 'ips': ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']}, 'fb': {'clicks': 3, 'dates': ['2022-01-01', '2022-01-02', '2022-01-03'], 'ips': ['192.168.1.1', '192.168.1.2', '192.168.1.3']}}
