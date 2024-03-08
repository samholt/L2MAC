import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	response = client.post('/event', json={
		'id': 1,
		'type': 'Birthday',
		'date': '2022-12-31',
		'time': '18:00:00',
		'theme': 'Hawaiian',
		'color_scheme': 'Blue and White'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Event created successfully'}


def test_create_event_invalid_data(client):
	response = client.post('/event', json={
		'id': 1,
		'type': 'Birthday',
		'date': '2022-12-31',
		'time': '18:00:00',
		'theme': 'Hawaiian'
	})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid data'}


def test_update_event(client):
	client.post('/event', json={
		'id': 1,
		'type': 'Birthday',
		'date': '2022-12-31',
		'time': '18:00:00',
		'theme': 'Hawaiian',
		'color_scheme': 'Blue and White'
	})
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Event updated successfully'}


def test_update_nonexistent_event(client):
	response = client.put('/event/999', json={'type': 'Wedding'})
	assert response.status_code == 404
	assert json.loads(response.data) == {'message': 'Event not found'}
