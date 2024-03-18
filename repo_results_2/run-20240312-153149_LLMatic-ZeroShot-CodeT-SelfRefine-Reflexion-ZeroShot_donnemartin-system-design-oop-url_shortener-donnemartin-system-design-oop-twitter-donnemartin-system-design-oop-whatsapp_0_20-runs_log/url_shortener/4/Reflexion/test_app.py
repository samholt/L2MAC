import pytest
from app import app
from database import users, urls


@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'short_url': 'ggl', 'user_id': '1', 'expiration_date': '2022-12-31'})
	assert response.status_code == 201
	assert response.get_json() == {'short_url': 'ggl'}
	assert 'ggl' in urls
	assert urls['ggl'].original_url == 'https://www.google.com'
	assert urls['ggl'].user_id == '1'
	assert urls['ggl'].expiration_date == '2022-12-31'
	assert '1' in users
	assert urls['ggl'] in users['1'].urls


def test_redirect_to_url(client):
	response = client.get('/ggl')
	assert response.status_code == 200


def test_get_user_urls(client):
	response = client.get('/user_urls/1')
	assert response.status_code == 200
	assert response.get_json() == {'urls': ['ggl']}


def test_get_all_data(client):
	response = client.get('/all_data')
	assert response.status_code == 200
	assert response.get_json() == {'users': {'1': ['ggl']}, 'urls': {'ggl': 'https://www.google.com'}}
