import pytest
from app import app
import json


def test_shorten_url():
	with app.test_client() as client:
		response = client.post('/shorten', json={'url': 'https://www.google.com'})
		assert response.status_code == 200
		assert 'short_url' in response.get_json()


def test_redirect_to_original():
	with app.test_client() as client:
		response = client.get('/test')
		assert response.status_code == 404


def test_view_analytics():
	with app.test_client() as client:
		response = client.get('/analytics/test')
		assert response.status_code == 200
		assert 'analytics' in response.get_json()


def test_create_user():
	with app.test_client() as client:
		response = client.post('/user/create', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert 'message' in response.get_json()


def test_login_user():
	with app.test_client() as client:
		response = client.post('/user/login', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert 'message' in response.get_json()


def test_logout_user():
	with app.test_client() as client:
		response = client.post('/user/logout', json={'username': 'test'})
		assert response.status_code == 200
		assert 'message' in response.get_json()


def test_view_all_urls():
	with app.test_client() as client:
		response = client.get('/admin/view_urls')
		assert response.status_code == 200
		assert 'urls' in response.get_json()
