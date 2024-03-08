import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Club created successfully'}


def test_join_club(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com'})
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers'})
	response = client.post('/join_club', json={'email': 'john@example.com', 'name': 'Book Club'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Joined club successfully'}


def test_list_clubs(client):
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers'})
	response = client.get('/list_clubs')
	assert response.status_code == 200
	assert 'Book Club' in json.loads(response.data)['clubs']


def test_list_users(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com'})
	response = client.get('/list_users')
	assert response.status_code == 200
	assert 'john@example.com' in json.loads(response.data)['users']
