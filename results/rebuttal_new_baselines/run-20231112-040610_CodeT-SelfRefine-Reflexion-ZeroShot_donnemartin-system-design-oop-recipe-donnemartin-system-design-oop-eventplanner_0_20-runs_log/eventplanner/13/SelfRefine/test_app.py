import pytest
import app
from app import Event, Venue, Guest, Vendor

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	response = client.post('/event', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Event created'}


def test_update_event(client):
	client.post('/event', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'})
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Event updated'}


def test_update_event_not_found(client):
	response = client.put('/event/999', json={'type': 'Wedding'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Event not found'}


def test_create_venue(client):
	response = client.post('/venue', json={'id': 1, 'name': 'Venue 1', 'location': 'Location 1', 'capacity': 100, 'type': 'Indoor'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Venue created'}


def test_update_venue(client):
	client.post('/venue', json={'id': 1, 'name': 'Venue 1', 'location': 'Location 1', 'capacity': 100, 'type': 'Indoor'})
	response = client.put('/venue/1', json={'name': 'Updated Venue'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Venue updated'}


def test_create_guest(client):
	response = client.post('/guest', json={'id': 1, 'name': 'Guest 1', 'email': 'guest1@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Guest created'}


def test_update_guest(client):
	client.post('/guest', json={'id': 1, 'name': 'Guest 1', 'email': 'guest1@example.com'})
	response = client.put('/guest/1', json={'name': 'Updated Guest'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Guest updated'}


def test_create_vendor(client):
	response = client.post('/vendor', json={'id': 1, 'name': 'Vendor 1', 'services': ['Service 1', 'Service 2']})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Vendor created'}


def test_update_vendor(client):
	client.post('/vendor', json={'id': 1, 'name': 'Vendor 1', 'services': ['Service 1', 'Service 2']})
	response = client.put('/vendor/1', json={'name': 'Updated Vendor'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Vendor updated'}
