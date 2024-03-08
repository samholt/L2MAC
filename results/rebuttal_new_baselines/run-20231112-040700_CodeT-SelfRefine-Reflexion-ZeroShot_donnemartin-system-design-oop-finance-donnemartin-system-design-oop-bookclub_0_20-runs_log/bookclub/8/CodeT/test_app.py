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


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'Test User', 'email': 'testuser@example.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_join_club(client):
	client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False})
	client.post('/create_user', json={'name': 'Test User', 'email': 'testuser@example.com'})
	response = client.post('/join_club', json={'user_name': 'Test User', 'club_name': 'Test Club'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User joined the club successfully'}


def test_join_private_club(client):
	client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': True})
	client.post('/create_user', json={'name': 'Test User', 'email': 'testuser@example.com'})
	response = client.post('/join_club', json={'user_name': 'Test User', 'club_name': 'Test Club'})
	assert response.status_code == 403
	assert json.loads(response.data) == {'message': 'This club is private'}
