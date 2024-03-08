import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_club(client):
	response = client.post('/create_club', data=json.dumps({'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Club created successfully'


def test_join_public_club(client):
	client.post('/create_club', data=json.dumps({'name': 'Public Club', 'description': 'A public club', 'is_private': False}), content_type='application/json')
	response = client.post('/join_club', data=json.dumps({'club_name': 'Public Club', 'user_name': 'John'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Joined club successfully'


def test_request_to_join_private_club(client):
	client.post('/create_club', data=json.dumps({'name': 'Private Club', 'description': 'A private club', 'is_private': True}), content_type='application/json')
	response = client.post('/join_club', data=json.dumps({'club_name': 'Private Club', 'user_name': 'John'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Request to join club sent'


def test_manage_request(client):
	client.post('/create_club', data=json.dumps({'name': 'Private Club', 'description': 'A private club', 'is_private': True}), content_type='application/json')
	client.post('/join_club', data=json.dumps({'club_name': 'Private Club', 'user_name': 'John'}), content_type='application/json')
	response = client.post('/manage_request', data=json.dumps({'club_name': 'Private Club', 'user_name': 'John', 'action': 'accept'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Request accepted'
