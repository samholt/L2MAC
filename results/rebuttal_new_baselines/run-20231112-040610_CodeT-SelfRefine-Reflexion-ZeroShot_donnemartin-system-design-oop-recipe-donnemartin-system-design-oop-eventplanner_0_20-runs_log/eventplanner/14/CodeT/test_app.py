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
		'type': 'Birthday',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Superhero',
		'color_scheme': 'Blue and Red'
	})
	assert response.status_code == 201
	assert 'id' in json.loads(response.data)


def test_update_event(client):
	client.post('/event', json={
		'type': 'Birthday',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Superhero',
		'color_scheme': 'Blue and Red'
	})
	response = client.put('/event/1', json={
		'type': 'Wedding'
	})
	assert response.status_code == 200
	assert 'message' in json.loads(response.data)
	assert json.loads(response.data)['message'] == 'Event updated'
