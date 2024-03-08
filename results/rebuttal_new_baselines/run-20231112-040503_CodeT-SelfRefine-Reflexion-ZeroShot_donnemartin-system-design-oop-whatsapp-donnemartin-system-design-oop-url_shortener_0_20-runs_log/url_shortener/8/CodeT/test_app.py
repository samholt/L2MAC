import pytest
import app
from flask import Flask
from dataclasses import dataclass
from datetime import datetime

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: []

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def mock_db():
	app.DB = {}
	return app.DB

def test_shorten_url(client, mock_db):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user'})
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()
	shortened_url = response.get_json()['shortened_url']
	assert shortened_url in mock_db
	assert mock_db[shortened_url].original == 'https://www.google.com'
	assert mock_db[shortened_url].user == 'test_user'

def test_redirect_url(client, mock_db):
	mock_db['test'] = URL('https://www.google.com', 'test', 'test_user', [])
	response = client.get('/test')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'
	assert len(mock_db['test'].clicks) == 1
