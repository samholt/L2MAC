import admin_dashboard
import url_shortener
import user_accounts
import analytics
import pytest

@pytest.fixture(autouse=True)
def setup():
	url_shortener.DATABASE.clear()
	user_accounts.USER_DB.clear()
	analytics.ANALYTICS_DB.clear()


def test_view_all_urls():
	url_shortener.DATABASE.update({'abc': 'http://google.com'})
	assert admin_dashboard.view_all_urls() == {'result': {'abc': 'http://google.com'}}


def test_delete_url():
	url_shortener.DATABASE.update({'abc': 'http://google.com'})
	assert admin_dashboard.delete_url('abc') == {'result': True}
	assert 'abc' not in url_shortener.DATABASE


def test_delete_user():
	user_accounts.USER_DB.update({'user1': {'password': 'pass', 'urls': []}})
	assert admin_dashboard.delete_user('user1') == {'result': True}
	assert 'user1' not in user_accounts.USER_DB


def test_view_system_performance():
	url_shortener.DATABASE.update({'abc': 'http://google.com', 'def': 'http://yahoo.com'})
	user_accounts.USER_DB.update({'user1': {'password': 'pass', 'urls': []}, 'user2': {'password': 'pass', 'urls': []}})
	analytics.ANALYTICS_DB.update({'abc': [{'time': 'now', 'location': 'USA'}], 'def': [{'time': 'now', 'location': 'USA'}]})
	assert admin_dashboard.view_system_performance() == {'result': {'number_of_urls': 2, 'number_of_users': 2, 'number_of_clicks': 2}}
