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
		'email': 'john@example.com',
		'clubs': {},
		'books_read': {},
		'following': {}
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'John Doe',
		'email': 'john@example.com',
		'clubs': {},
		'books_read': {},
		'following': {}
	}


def test_get_user(client):
	response = client.get('/user/1')
	assert response.status_code == 200
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'John Doe',
		'email': 'john@example.com',
		'clubs': {},
		'books_read': {},
		'following': {}
	}


def test_update_user(client):
	response = client.put('/user/1', json={
		'id': '1',
		'name': 'Jane Doe',
		'email': 'jane@example.com',
		'clubs': {},
		'books_read': {},
		'following': {}
	})
	assert response.status_code == 200
	assert json.loads(response.data) == {
		'id': '1',
		'name': 'Jane Doe',
		'email': 'jane@example.com',
		'clubs': {},
		'books_read': {},
		'following': {}
	}


def test_delete_user(client):
	response = client.delete('/user/1')
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'User deleted'}

# Similar tests for Club, Book, Meeting, Discussion, Resource
