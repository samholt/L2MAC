import pytest
from flask import Flask
from app import app as flask_app

@pytest.fixture
def client():
	flask_app.config['TESTING'] = True
	with flask_app.test_client() as client:
		yield client

def test_shorten_url(client):
	response = client.post('/shorten', data={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'Short URL: ' in response.data.decode()

def test_redirect_to_url(client):
	response = client.post('/shorten', data={'url': 'https://www.google.com'})
	short_url = response.data.decode().split(': ')[1]
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'

def test_get_analytics(client):
	response = client.post('/shorten', data={'url': 'https://www.google.com'})
	short_url = response.data.decode().split(': ')[1]
	client.get(f'/{short_url}')
	response = client.get(f'/analytics/{short_url}')
	assert 'clicks' in response.json
	assert response.json['clicks'] == 1
	assert 'click_data' in response.json
	assert isinstance(response.json['click_data'], list)
	assert len(response.json['click_data']) == 1
	assert 'time' in response.json['click_data'][0]
	assert 'location' in response.json['click_data'][0]
	assert response.json['click_data'][0]['location'] == '127.0.0.1'
