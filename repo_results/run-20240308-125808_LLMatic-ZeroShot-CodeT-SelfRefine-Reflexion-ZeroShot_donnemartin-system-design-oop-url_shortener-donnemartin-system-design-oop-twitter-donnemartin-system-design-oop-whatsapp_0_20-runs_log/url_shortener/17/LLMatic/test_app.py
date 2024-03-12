import pytest
import app
from flask import url_for

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200


def test_redirect_to_url(client):
	app.url_db['test'] = {'url': 'http://example.com', 'expiration_datetime': None}
	response = client.get('/test')
	assert response.status_code == 302


def test_shorten_url(client):
	response = client.post('/shorten_url', data={'url': 'http://example.com'})
	assert response.status_code == 200


def test_analytics(client):
	response = client.get('/analytics/test')
	assert response.status_code == 200


def test_create_account(client):
	response = client.post('/create_account', data={'username': 'test'})
	assert response.status_code == 200


def test_add_url(client):
	response = client.post('/add_url', data={'username': 'test', 'url': 'http://example.com'})
	assert response.status_code == 200


def test_view_urls(client):
	response = client.get('/view_urls/test')
	assert response.status_code == 200


def test_delete_url(client):
	response = client.delete('/delete_url', data={'username': 'test', 'url': 'http://example.com'})
	assert response.status_code == 200


def test_edit_url(client):
	response = client.put('/edit_url', data={'username': 'test', 'old_url': 'http://example.com', 'new_url': 'http://example.org'})
	assert response.status_code == 200


def test_admin_view_all_urls(client):
	response = client.get('/admin/view_all_urls')
	assert response.status_code == 200


def test_admin_delete_url(client):
	response = client.delete('/admin/delete_url', data={'short_url': 'test'})
	assert response.status_code == 200


def test_admin_delete_user(client):
	response = client.delete('/admin/delete_user', data={'username': 'test'})
	assert response.status_code == 200


def test_admin_monitor_system(client):
	response = client.get('/admin/monitor_system')
	assert response.status_code == 200
