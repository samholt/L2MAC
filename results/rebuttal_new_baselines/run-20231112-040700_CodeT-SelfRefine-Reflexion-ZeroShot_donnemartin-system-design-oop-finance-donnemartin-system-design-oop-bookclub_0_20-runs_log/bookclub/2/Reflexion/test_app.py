import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/users', json={
		'id': '1',
		'name': 'Test User',
		'email': 'test@example.com'
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'Test User',
		'email': 'test@example.com'
	}

def test_create_club(client):
	response = client.post('/clubs', json={
		'id': '1',
		'name': 'Test Club',
		'description': 'This is a test club.',
		'is_private': False
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'Test Club',
		'description': 'This is a test club.',
		'is_private': False
	}

def test_create_meeting(client):
	response = client.post('/meetings', json={
		'id': '1',
		'club_id': '1',
		'date': '2022-01-01'
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'club_id': '1',
		'date': '2022-01-01'
	}

def test_create_book(client):
	response = client.post('/books', json={
		'id': '1',
		'title': 'Test Book',
		'author': 'Test Author'
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'title': 'Test Book',
		'author': 'Test Author'
	}
