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
	assert response.get_json()['message'] == 'Club created successfully'


def test_join_club(client):
	app.users['Test User'] = app.User('Test User', {})
	response = client.post('/join_club', data=json.dumps({'club_name': 'Test Club', 'user_name': 'Test User'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Joined club successfully'
