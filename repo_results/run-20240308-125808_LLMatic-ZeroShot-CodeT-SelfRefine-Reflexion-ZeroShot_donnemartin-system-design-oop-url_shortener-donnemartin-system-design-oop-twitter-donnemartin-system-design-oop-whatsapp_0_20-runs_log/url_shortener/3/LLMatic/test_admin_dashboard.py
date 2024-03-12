import pytest
from admin_dashboard import AdminDashboard
from database import url_db
from analytics import get_analytics_db
from user_accounts import UserAccount


def setup_function():
	global admin
	admin = AdminDashboard()
	url_db.clear()
	get_analytics_db().clear()
	admin.user_account.accounts.clear()


def test_view_all_urls():
	url_db['short1'] = 'http://example.com'
	assert admin.view_all_urls() == url_db


def test_delete_url():
	url_db['short1'] = 'http://example.com'
	assert admin.delete_url('short1') == 'URL deleted successfully'
	assert 'short1' not in url_db


def test_delete_user():
	admin.user_account.create_account('user1', 'password1')
	assert admin.delete_user('user1') == 'User deleted successfully'
	assert 'user1' not in admin.user_account.accounts


def test_view_system_performance():
	get_analytics_db()['short1'] = [{'time': '2022-01-01T00:00:00', 'location': 'USA'}]
	assert admin.view_system_performance() == get_analytics_db()

