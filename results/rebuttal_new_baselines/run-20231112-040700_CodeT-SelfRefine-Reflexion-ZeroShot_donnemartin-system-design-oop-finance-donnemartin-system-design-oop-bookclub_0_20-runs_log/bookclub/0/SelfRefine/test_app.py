import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', data=json.dumps({'name': 'Test User', 'email': 'test@example.com'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User created successfully'
	response = client.post('/create_user', data=json.dumps({'name': 'Test User', 'email': 'test@example.com'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'User already exists'


def test_create_club(client):
	response = client.post('/create_club', data=json.dumps({'name': 'Test Club', 'description': 'This is a test club', 'is_private': False}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Club created successfully'
	response = client.post('/create_club', data=json.dumps({'name': 'Test Club', 'description': 'This is a test club', 'is_private': False}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Club already exists'


def test_join_club(client):
	app.users['Test User'] = app.User('Test User', 'test@example.com', {})
	app.clubs['Test Club'] = app.Club('Test Club', 'This is a test club', False, {})
	response = client.post('/join_club', data=json.dumps({'user_name': 'Test User', 'club_name': 'Test Club'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Joined club successfully'
	response = client.post('/join_club', data=json.dumps({'user_name': 'Test User', 'club_name': 'Test Club'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'User is already a member of the club'
