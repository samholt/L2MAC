import pytest
from app import app
from url_shortener import url_database
from user_accounts import users
from analytics import analytics_database

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200

def test_shorten_url(client):
	response = client.post('/shorten_url', json={'url': 'https://www.google.com', 'username': 'test'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

def test_redirect_to_url(client):
	short_url = list(url_database.keys())[0]
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

def test_view_analytics(client):
	short_url = list(url_database.keys())[0]
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert 'statistics' in response.get_json()

def test_view_user_urls(client):
	response = client.get('/user/test')
	assert response.status_code == 200
	assert 'urls' in response.get_json()

def test_admin_view_all_urls(client):
	response = client.get('/admin/view_all_urls')
	assert response.status_code == 200
	assert 'urls' in response.get_json()

def test_admin_delete_user(client):
	response = client.delete('/admin/delete_user/test')
	assert response.status_code == 200
	assert response.get_json()['success'] == True

