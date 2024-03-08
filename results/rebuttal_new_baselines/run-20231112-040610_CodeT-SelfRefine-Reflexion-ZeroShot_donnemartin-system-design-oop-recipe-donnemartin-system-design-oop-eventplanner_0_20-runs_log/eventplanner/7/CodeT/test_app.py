import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	response = client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_get_event(client):
	client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'})
	response = client.get('/event/1')
	assert response.status_code == 200
	assert response.get_json()['id'] == 1


def test_update_event(client):
	client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'})
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 200
	assert response.get_json()['type'] == 'Wedding'
