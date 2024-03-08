import pytest
from unittest.mock import MagicMock
from flask.testing import FlaskClient
from app import app, url_shortener, user_accounts, analytics


def test_hello_world():
	with app.test_client() as c:
		response = c.get('/')
		assert response.data == b'Hello, World!'


def test_redirect_to_url():
	with app.test_client() as c:
		url_shortener.get_original_url = MagicMock(return_value='http://original-url.com')
		response = c.get('/short-url')
		assert response.status_code == 302
		assert response.location == 'http://original-url.com'


def test_view_all_urls():
	with app.test_client() as c:
		url_shortener.get_all_urls = MagicMock(return_value={'short-url': 'http://original-url.com'})
		response = c.get('/admin/urls')
		assert response.json == {'short-url': 'http://original-url.com'}


def test_delete_url():
	with app.test_client() as c:
		url_shortener.delete_url = MagicMock(return_value='URL deleted successfully')
		response = c.get('/admin/delete_url/short-url')
		assert response.data == b'URL deleted successfully'


def test_delete_account():
	with app.test_client() as c:
		user_accounts.delete_account = MagicMock(return_value='Account deleted successfully')
		response = c.get('/admin/delete_account/username')
		assert response.data == b'Account deleted successfully'


def test_view_analytics():
	with app.test_client() as c:
		analytics.get_all_data = MagicMock(return_value={'short-url': {'clicks': 10, 'click_details': []}})
		response = c.get('/admin/analytics')
		assert response.json == {'short-url': {'clicks': 10, 'click_details': []}}

