import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', data=json.dumps({'id': '1', 'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 201
	assert b'User created successfully' in response.data
