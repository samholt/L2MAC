import pytest
from main import app
from services import validate_and_shorten_url, create_user


def test_home():
	with app.test_client() as client:
		response = client.get('/')
		assert response.status_code == 200


def test_shorten_url():
	with app.test_client() as client:
		response = client.post('/shorten', json={'url': 'https://www.google.com'})
		assert response.status_code == 200


def test_redirect_to_original():
	with app.test_client() as client:
		short_url = validate_and_shorten_url('https://www.google.com')
		response = client.get(f'/{short_url}')
		assert response.status_code == 302


def test_get_click_stats():
	with app.test_client() as client:
		short_url = validate_and_shorten_url('https://www.google.com')
		response = client.get(f'/{short_url}/stats')
		assert response.status_code == 200


def test_register():
	with app.test_client() as client:
		response = client.post('/register', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200


def test_login():
	with app.test_client() as client:
		create_user('test', 'test')
		response = client.post('/login', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200


def test_get_urls():
	with app.test_client() as client:
		create_user('test', 'test')
		validate_and_shorten_url('https://www.google.com', 'test')
		response = client.get('/user/urls', json={'username': 'test'})
		assert response.status_code == 200


def test_admin_get_urls():
	with app.test_client() as client:
		response = client.get('/admin/urls')
		assert response.status_code == 200


def test_admin_delete_url():
	with app.test_client() as client:
		short_url = validate_and_shorten_url('https://www.google.com')
		response = client.delete(f'/admin/urls/{short_url}')
		assert response.status_code == 200


def test_admin_get_users():
	with app.test_client() as client:
		response = client.get('/admin/users')
		assert response.status_code == 200


def test_admin_delete_user():
	with app.test_client() as client:
		create_user('test', 'test')
		response = client.delete('/admin/users/test')
		assert response.status_code == 200

