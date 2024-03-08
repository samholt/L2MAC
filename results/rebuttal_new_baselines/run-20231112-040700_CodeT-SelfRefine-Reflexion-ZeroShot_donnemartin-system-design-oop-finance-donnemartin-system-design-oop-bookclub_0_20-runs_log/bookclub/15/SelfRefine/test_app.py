import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'Test User', 'email': 'test@example.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_create_club(client):
	client.post('/create_user', json={'name': 'Test User', 'email': 'test@example.com'})
	response = client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'creator_email': 'test@example.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Club created successfully'}


def test_create_club_without_user(client):
	response = client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'creator_email': 'nonexistent@example.com'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'User does not exist'}


def test_add_member(client):
	client.post('/create_user', json={'name': 'Test User', 'email': 'test@example.com'})
	client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'creator_email': 'test@example.com'})
	response = client.post('/add_member', json={'club_name': 'Test Club', 'member_email': 'test@example.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Member added successfully'}


def test_add_existing_member(client):
	client.post('/create_user', json={'name': 'Test User', 'email': 'test@example.com'})
	client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'creator_email': 'test@example.com'})
	client.post('/add_member', json={'club_name': 'Test Club', 'member_email': 'test@example.com'})
	response = client.post('/add_member', json={'club_name': 'Test Club', 'member_email': 'test@example.com'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Member already exists in the club'}
