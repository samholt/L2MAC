import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Club created successfully'}


def test_join_club(client):
	client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False})
	response = client.post('/join_club', json={'club_name': 'Test Club', 'user_name': 'Test User', 'user_email': 'test@example.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Joined club successfully'}


def test_invite_to_club(client):
	client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': True})
	response = client.post('/invite_to_club', json={'club_name': 'Test Club', 'user_email': 'test@example.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User invited successfully'}
