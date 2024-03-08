import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_event(client):
	response = client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	id = response.get_json()['id']

	response = client.get(f'/event/{id}')
	assert response.status_code == 200
	assert response.get_json() == {'id': id, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}

	response = client.put(f'/event/{id}', json={'theme': 'Ocean', 'color_scheme': 'Green'})
	assert response.status_code == 200
	assert response.get_json() == {'id': id, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Ocean', 'color_scheme': 'Green'}

	response = client.get(f'/event/{id}')
	assert response.status_code == 200
	assert response.get_json() == {'id': id, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Ocean', 'color_scheme': 'Green'}
