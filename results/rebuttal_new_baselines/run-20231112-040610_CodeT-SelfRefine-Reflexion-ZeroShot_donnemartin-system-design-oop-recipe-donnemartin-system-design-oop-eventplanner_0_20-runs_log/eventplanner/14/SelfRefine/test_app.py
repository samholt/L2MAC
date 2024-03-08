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
		'id': '1',
		'type': 'Birthday',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Superhero',
		'color_scheme': 'Blue and Red'
	})
	assert response.status_code == 201
	assert json.loads(response.data) == {
		'id': '1',
		'type': 'Birthday',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Superhero',
		'color_scheme': 'Blue and Red'
	}


def test_create_existing_event(client):
	client.post('/event', json={
		'id': '1',
		'type': 'Birthday',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Superhero',
		'color_scheme': 'Blue and Red'
	})
	response = client.post('/event', json={
		'id': '1',
		'type': 'Birthday',
		'date': '2022-12-13',
		'time': '18:00',
		'theme': 'Superhero',
		'color_scheme': 'Blue and Red'
	})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Event already exists'}


def test_update_event(client):
	client.post('/event', json={
		'id': '1',
		'type': 'Birthday',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Superhero',
		'color_scheme': 'Blue and Red'
	})
	response = client.put('/event/1', json={
		'id': '1',
		'type': 'Birthday',
		'date': '2022-12-13',
		'time': '18:00',
		'theme': 'Superhero',
		'color_scheme': 'Blue and Red'
	})
	assert response.status_code == 200
	assert json.loads(response.data) == {
		'id': '1',
		'type': 'Birthday',
		'date': '2022-12-13',
		'time': '18:00',
		'theme': 'Superhero',
		'color_scheme': 'Blue and Red'
	}


def test_update_nonexistent_event(client):
	response = client.put('/event/2', json={
		'id': '2',
		'type': 'Birthday',
		'date': '2022-12-13',
		'time': '18:00',
		'theme': 'Superhero',
		'color_scheme': 'Blue and Red'
	})
	assert response.status_code == 404
	assert json.loads(response.data) == {'error': 'Event not found'}
