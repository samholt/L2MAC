import pytest
import datetime
from url_shortener import URLShortener
from analytics import Analytics
from admin_dashboard import AdminDashboard
from user_accounts import UserAccounts

url_shortener = URLShortener()
analytics = Analytics()
admin_dashboard = AdminDashboard()
user_accounts = UserAccounts()


def test_view_all_urls():
	url_shortener.generate_short_url('https://example.com')
	assert len(admin_dashboard.view_all_urls()) >= 1


def test_view_user_accounts():
	user_accounts.create_account('test')
	assert len(admin_dashboard.view_user_accounts()) >= 1


def test_view_analytics():
	short_url = url_shortener.generate_short_url('https://example3.com')
	analytics.track_click(short_url, '127.0.0.1')
	assert len(admin_dashboard.view_analytics()) >= 1


def test_delete_url():
	short_url = url_shortener.generate_short_url('https://example4.com')
	admin_dashboard.delete_url(short_url)
	assert short_url not in admin_dashboard.view_all_urls()


def test_delete_user():
	user_accounts.create_account('test2')
	admin_dashboard.delete_user('test2')
	assert 'test2' not in admin_dashboard.view_user_accounts()
