import pytest
import app
from app import Event, Venue, Guest, Vendor

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('event', [
	{'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00'},
	{'id': 2, 'type': 'Wedding', 'date': '2023-01-01', 'time': '12:00'}
])
def test_create_event(client, event):
	response = client.post('/events', json=event)
	assert response.status_code == 201
	assert response.get_json() == {'id': event['id']}

@pytest.mark.parametrize('venue', [
	{'id': 1, 'location': 'New York', 'capacity': 100, 'type': 'Hall'},
	{'id': 2, 'location': 'Los Angeles', 'capacity': 200, 'type': 'Outdoor'}
])
def test_create_venue(client, venue):
	response = client.post('/venues', json=venue)
	assert response.status_code == 201
	assert response.get_json() == {'id': venue['id']}

@pytest.mark.parametrize('guest', [
	{'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
	{'id': 2, 'name': 'Jane Doe', 'email': 'jane@example.com'}
])
def test_create_guest(client, guest):
	response = client.post('/guests', json=guest)
	assert response.status_code == 201
	assert response.get_json() == {'id': guest['id']}

@pytest.mark.parametrize('vendor', [
	{'id': 1, 'name': 'Catering Co.', 'service': 'Catering'},
	{'id': 2, 'name': 'Decorations Inc.', 'service': 'Decorations'}
])
def test_create_vendor(client, vendor):
	response = client.post('/vendors', json=vendor)
	assert response.status_code == 201
	assert response.get_json() == {'id': vendor['id']}
