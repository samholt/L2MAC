import pytest
import app
import url_shortener
from datetime import datetime


def test_shorten_url():
	url_shortener.DATABASE = {}
	with app.app.test_request_context('/shorten', method='POST', data={'url': 'http://example.com'}):
		response = app.shorten_url()
		assert response in url_shortener.DATABASE.values()


def test_redirect():
	url_shortener.DATABASE = {'http://example.com': 'abc123'}
	with app.app.test_request_context('/abc123'):
		response = app.redirect_to_url('abc123')
		assert response.status_code == 302
		assert response.location == 'http://example.com'


def test_analytics():
	url_shortener.DATABASE['http://example.com'] = 'abc123'
	with app.app.test_request_context('/analytics/abc123'):
		app.track_click('abc123', '127.0.0.1')
		response = app.analytics('abc123')
		assert len(eval(response.replace('datetime.datetime', 'datetime'))) == 1


def test_user_accounts():
	app.user_accounts.USER_DATABASE = {}
	with app.app.test_request_context('/user/create', method='POST', data={'username': 'test', 'password': 'test'}):
		response = app.create_user()
		assert response == 'Account created successfully.'

	with app.app.test_request_context('/user/add_url', method='POST', data={'username': 'test', 'password': 'test', 'url': 'http://example.com'}):
		response = app.add_url()
		assert response == 'URL added successfully.'

	with app.app.test_request_context('/user/view_urls', method='POST', data={'username': 'test', 'password': 'test'}):
		response = app.view_urls()
		assert 'http://example.com' in response

	with app.app.test_request_context('/user/delete_url', method='POST', data={'username': 'test', 'password': 'test', 'url': 'http://example.com'}):
		response = app.user_delete_url()
		assert response == 'URL deleted successfully.'


def test_admin_dashboard():
	app.user_accounts.USER_DATABASE = {'admin': {'password': 'admin', 'role': 'admin'}}
	with app.app.test_request_context('/admin/view_all_urls'):
		response = app.admin_view_all_urls()
		assert 'http://example.com' in response

	with app.app.test_request_context('/admin/delete_url', method='POST', data={'url': 'http://example.com'}):
		response = app.admin_delete_url()
		assert response == 'URL deleted successfully.'

	with app.app.test_request_context('/admin/delete_user', method='POST', data={'username': 'test'}):
		response = app.admin_delete_user()
		assert response == 'User deleted successfully.'

	with app.app.test_request_context('/admin/monitor_system'):
		response = app.admin_monitor_system()
		assert response == '{}'




