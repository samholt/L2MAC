import pytest
import app
from app import Event, Venue, Guest, Vendor

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def init_db():
	app.DB = {'events': [], 'venues': [], 'guests': [], 'vendors': []}

def test_create_event(client, init_db):
	event = {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}
	response = client.post('/event', json=event)
	assert response.status_code == 201
	assert response.get_json() == event

def test_create_venue(client, init_db):
	venue = {'id': 1, 'name': 'Grand Hall', 'location': 'New York', 'capacity': 500, 'type': 'Indoor'}
	response = client.post('/venue', json=venue)
	assert response.status_code == 201
	assert response.get_json() == venue

def test_create_guest(client, init_db):
	guest = {'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'}
	response = client.post('/guest', json=guest)
	assert response.status_code == 201
	assert response.get_json() == guest

def test_create_vendor(client, init_db):
	vendor = {'id': 1, 'name': 'Catering Co.', 'service': 'Catering'}
	response = client.post('/vendor', json=vendor)
	assert response.status_code == 201
	assert response.get_json() == vendor
