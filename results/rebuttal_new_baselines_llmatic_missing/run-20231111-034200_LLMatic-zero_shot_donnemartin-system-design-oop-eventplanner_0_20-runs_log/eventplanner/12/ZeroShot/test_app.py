import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	data = {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}
	response = client.post('/event', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == data


def test_get_event(client):
	data = {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}
	client.post('/event', data=json.dumps(data), content_type='application/json')
	response = client.get('/event/1')
	assert response.status_code == 200
	assert response.get_json() == data


def test_get_event_not_found(client):
	response = client.get('/event/999')
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Event not found'}
