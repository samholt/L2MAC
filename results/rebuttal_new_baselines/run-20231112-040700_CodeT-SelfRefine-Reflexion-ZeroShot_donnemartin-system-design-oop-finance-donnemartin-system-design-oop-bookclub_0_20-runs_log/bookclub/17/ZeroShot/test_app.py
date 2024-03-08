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


def test_create_club(client):
	client.post('/create_user', data=json.dumps({'name': 'Test User', 'email': 'test@example.com'}), content_type='application/json')
	response = client.post('/create_club', data=json.dumps({'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'creator_email': 'test@example.com'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Club created successfully'
