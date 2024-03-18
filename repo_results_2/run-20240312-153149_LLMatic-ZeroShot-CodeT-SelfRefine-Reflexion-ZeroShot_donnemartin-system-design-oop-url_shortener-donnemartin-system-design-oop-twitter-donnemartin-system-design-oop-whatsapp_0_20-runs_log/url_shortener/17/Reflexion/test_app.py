import pytest
import app
import json
from flask import Flask
from werkzeug.exceptions import NotFound

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_data():
	app.urls_db = {}
	app.users_db = {}

@pytest.mark.usefixtures('reset_data')
def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_redirect_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.usefixtures('reset_data')
def test_redirect_url_not_found(client):
	response = client.get('/nonexistent')
	assert response.status_code == 404

@pytest.mark.usefixtures('reset_data')
def test_create_user(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_get_user(client):
	client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.get('/user/test')
	assert response.status_code == 200
	assert 'username' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_get_user_not_found(client):
	response = client.get('/user/nonexistent')
	assert response.status_code == 404

@pytest.mark.usefixtures('reset_data')
def test_delete_user(client):
	client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.delete('/user/test')
	assert response.status_code == 200
	assert 'message' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_delete_user_not_found(client):
	response = client.delete('/user/nonexistent')
	assert response.status_code == 404

@pytest.mark.usefixtures('reset_data')
def test_get_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/url/{short_url}')
	assert response.status_code == 200
	assert 'original' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_get_url_not_found(client):
	response = client.get('/url/nonexistent')
	assert response.status_code == 404

@pytest.mark.usefixtures('reset_data')
def test_delete_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.delete(f'/url/{short_url}')
	assert response.status_code == 200
	assert 'message' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_delete_url_not_found(client):
	response = client.delete('/url/nonexistent')
	assert response.status_code == 404

@pytest.mark.usefixtures('reset_data')
def test_admin_dashboard(client):
	response = client.get('/admin')
	assert response.status_code == 200
	assert 'users' in response.get_json()
	assert 'urls' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_admin_delete_user(client):
	client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.delete('/admin/user/test')
	assert response.status_code == 200
	assert 'message' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_admin_delete_user_not_found(client):
	response = client.delete('/admin/user/nonexistent')
	assert response.status_code == 404

@pytest.mark.usefixtures('reset_data')
def test_admin_delete_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.delete(f'/admin/url/{short_url}')
	assert response.status_code == 200
	assert 'message' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_admin_delete_url_not_found(client):
	response = client.delete('/admin/url/nonexistent')
	assert response.status_code == 404

@pytest.mark.usefixtures('reset_data')
def test_set_url_expiry(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.post(f'/url/{short_url}/expire', data=json.dumps({'expiry_date': '2022-12-31'}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()

@pytest.mark.usefixtures('reset_data')
def test_set_url_expiry_not_found(client):
	response = client.post('/url/nonexistent/expire', data=json.dumps({'expiry_date': '2022-12-31'}), content_type='application/json')
	assert response.status_code == 404
