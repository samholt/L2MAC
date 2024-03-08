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
	assert response.get_json() == {'id': 1}


def test_create_event_missing_field(client):
	response = client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney'})
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Missing required field'}


def test_get_event(client):
	client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'})
	response = client.get('/event/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'}


def test_get_event_not_found(client):
	response = client.get('/event/999')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'Event not found'}


def test_update_event(client):
	client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'})
	response = client.put('/event/1', json={'theme': 'Marvel'})
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Marvel', 'color_scheme': 'Blue'}


def test_delete_event(client):
	client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'})
	response = client.delete('/event/1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Event deleted'}


def test_get_events(client):
	client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'})
	response = client.get('/events')
	assert response.status_code == 200
	assert len(response.get_json()) == 1
