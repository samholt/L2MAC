import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/user', json={
		'id': '1',
		'name': 'John Doe',
		'email': 'john.doe@example.com',
		'clubs': {},
		'books_read': {},
		'books_to_read': {},
		'follows': {}
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'John Doe',
		'email': 'john.doe@example.com',
		'clubs': {},
		'books_read': {},
		'books_to_read': {},
		'follows': {}
	}

# Similar tests can be written for the other endpoints
