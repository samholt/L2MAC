import pytest
import app
from app import Event, Venue, Guest, Vendor

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {'events': [], 'venues': [], 'guests': [], 'vendors': []}

def test_create_event(client, reset_db):
	event = {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}
	response = client.post('/event', json=event)
	assert response.status_code == 201
	assert response.get_json() == event

	response = client.get('/event/1')
	assert response.status_code == 200
	assert response.get_json() == event

	updated_event = {'type': 'Wedding'}
	response = client.put('/event/1', json=updated_event)
	assert response.status_code == 200
	event.update(updated_event)
	assert response.get_json() == event

	response = client.get('/event/1')
	assert response.status_code == 200
	assert response.get_json() == event
