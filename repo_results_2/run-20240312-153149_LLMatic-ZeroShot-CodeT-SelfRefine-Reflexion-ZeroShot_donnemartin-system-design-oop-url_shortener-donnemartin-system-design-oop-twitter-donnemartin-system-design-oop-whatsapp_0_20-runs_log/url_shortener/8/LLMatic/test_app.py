import pytest
from app import create_app
from url_shortener import URLShortener
from user import User
from admin import Admin


@pytest.fixture
def client():
	app = create_app()
	app.config['TESTING'] = True

	with app.test_client() as client:
		yield client


def test_redirect_to_url(client):
	response = client.get('/nonexistent_url')
	assert response.status_code == 404


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_create_user(client):
	response = client.post('/user/create', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User created successfully'}


def test_add_url(client):
	response = client.post('/user/add_url', json={'username': 'test', 'long_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_view_urls(client):
	response = client.get('/user/view_urls?username=test')
	assert response.status_code == 200


def test_edit_url(client):
	response = client.put('/user/edit_url', json={'username': 'test', 'short_url': 'test', 'new_long_url': 'https://www.google.com'})
	assert response.status_code == 200


def test_delete_url(client):
	response = client.delete('/user/delete_url', json={'username': 'test', 'short_url': 'test'})
	assert response.status_code == 200


def test_view_analytics(client):
	response = client.get('/user/view_analytics?username=test&short_url=test')
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)
	assert 'clicks' in response.get_json() or 'message' in response.get_json()


def test_view_all_urls(client):
	response = client.get('/admin/view_all_urls')
	assert response.status_code == 200


def test_admin_delete_url(client):
	response = client.delete('/admin/delete_url', json={'short_url': 'test'})
	assert response.status_code == 200


def test_delete_user(client):
	response = client.delete('/admin/delete_user', json={'username': 'test'})
	assert response.status_code == 200


def test_monitor_system(client):
	response = client.get('/admin/monitor_system')
	assert response.status_code == 200
