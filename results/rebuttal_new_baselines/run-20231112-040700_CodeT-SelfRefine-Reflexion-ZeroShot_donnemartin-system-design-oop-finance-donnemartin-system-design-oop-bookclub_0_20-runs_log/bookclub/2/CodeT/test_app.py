import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': []})
	assert response.status_code == 201
	assert json.loads(response.data) == {'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': []}


def test_join_club(client):
	client.post('/create_user', json={'name': 'Test User', 'clubs': []})
	client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': []})
	response = client.post('/join_club', json={'club_name': 'Test Club', 'user_name': 'Test User'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'Joined club'}


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'Test User', 'clubs': []})
	assert response.status_code == 201
	assert json.loads(response.data) == {'name': 'Test User', 'clubs': []}
