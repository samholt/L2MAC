import pytest
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_home(client):
	response = client.get('/')
	assert response.status_code == 200

def test_redirect_to_url(client):
	response = client.get('/test')
	assert response.status_code == 404

def test_create_account(client):
	response = client.post('/create_account', data={'username': 'test', 'password': 'test'})
	assert response.data == b'Account created successfully.'

def test_view_urls(client):
	response = client.post('/view_urls', data={'username': 'test', 'password': 'test'})
	assert response.data == b'[]\n'

def test_edit_url(client):
	response = client.post('/edit_url', data={'username': 'test', 'password': 'test', 'old_url': 'old', 'new_url': 'new'})
	assert response.data == b'URL not found.'

def test_delete_url(client):
	response = client.post('/delete_url', data={'username': 'test', 'password': 'test', 'url': 'test'})
	assert response.data == b'URL not found.'

def test_view_analytics(client):
	response = client.post('/view_analytics', data={'username': 'test', 'password': 'test'})
	assert response.data == b'[]\n'

def test_admin_view_all_urls(client):
	response = client.get('/admin/view_all_urls')
	assert response.data == b'[]\n'

def test_admin_delete_url(client):
	response = client.post('/admin/delete_url', data={'url': 'test'})
	assert response.data == b'URL not found.'

def test_admin_delete_user(client):
	response = client.post('/admin/delete_user', data={'username': 'test'})
	assert response.data == b'User not found.'

def test_admin_view_analytics(client):
	response = client.get('/admin/view_analytics')
	assert response.data == b'{}\n'
