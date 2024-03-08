import pytest
from search import app
from flask import json

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_search(client):
	response = client.post('/search', json={'search_term': 'test'}, headers={'Authorization': 'test@test.com'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'users' in data
	assert 'posts' in data
