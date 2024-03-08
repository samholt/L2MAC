import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'id': '1', 'name': 'John Doe', 'email': 'john@example.com', 'clubs': []})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'name': 'John Doe', 'email': 'john@example.com', 'clubs': []}


def test_create_club(client):
	response = client.post('/create_club', json={'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers.', 'is_private': False, 'members': []})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers.', 'is_private': False, 'members': []}


def test_join_club(client):
	client.post('/create_user', json={'id': '1', 'name': 'John Doe', 'email': 'john@example.com', 'clubs': []})
	client.post('/create_club', json={'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers.', 'is_private': False, 'members': []})
	response = client.post('/join_club', json={'user_id': '1', 'club_id': '1'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Successfully joined the club.'}
