import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_club(client):
	response = client.post('/create_club', data=json.dumps({'name': 'Test Club', 'description': 'This is a test club', 'is_private': False}), content_type='application/json')
	assert response.status_code == 201
	assert b'Club created successfully' in response.data

	# Test for duplicate club
	response = client.post('/create_club', data=json.dumps({'name': 'Test Club', 'description': 'This is a test club', 'is_private': False}), content_type='application/json')
	assert response.status_code == 400
	assert b'Club already exists' in response.data


def test_join_club(client):
	client.post('/create_user', data=json.dumps({'name': 'Test User 1'}), content_type='application/json')
	client.post('/create_club', data=json.dumps({'name': 'Test Club', 'description': 'This is a test club', 'is_private': False}), content_type='application/json')
	response = client.post('/join_club', data=json.dumps({'user_name': 'Test User 1', 'club_name': 'Test Club'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Joined club successfully' in response.data


def test_create_user(client):
	response = client.post('/create_user', data=json.dumps({'name': 'Test User 2'}), content_type='application/json')
	assert response.status_code == 201
	assert b'User created successfully' in response.data

	# Test for duplicate user
	response = client.post('/create_user', data=json.dumps({'name': 'Test User 3'}), content_type='application/json')
	assert response.status_code == 201
	assert b'User created successfully' in response.data
