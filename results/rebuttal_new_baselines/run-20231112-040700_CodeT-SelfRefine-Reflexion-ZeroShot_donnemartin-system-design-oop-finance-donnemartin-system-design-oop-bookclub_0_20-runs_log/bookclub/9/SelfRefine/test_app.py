import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_club(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
	response = client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'owner_name': 'John Doe'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Club created successfully'}


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_join_club(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'owner_name': 'John Doe'})
	response = client.post('/join_club', json={'user_name': 'John Doe', 'club_name': 'Book Club'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User joined the club successfully'}


def test_join_private_club(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
	client.post('/create_user', json={'name': 'Jane Doe', 'email': 'jane.doe@example.com'})
	client.post('/create_club', json={'name': 'Private Club', 'description': 'A private club', 'is_private': True, 'owner_name': 'John Doe'})
	response = client.post('/join_club', json={'user_name': 'Jane Doe', 'club_name': 'Private Club'})
	assert response.status_code == 403
	assert response.get_json() == {'message': 'This club is private'}


def test_join_nonexistent_club_or_user(client):
	response = client.post('/join_club', json={'user_name': 'Nonexistent User', 'club_name': 'Nonexistent Club'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User or club not found'}


def test_join_club_already_member(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'owner_name': 'John Doe'})
	client.post('/join_club', json={'user_name': 'John Doe', 'club_name': 'Book Club'})
	response = client.post('/join_club', json={'user_name': 'John Doe', 'club_name': 'Book Club'})
	assert response.status_code == 409
	assert response.get_json() == {'message': 'User is already a member of this club'}
