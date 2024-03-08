import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def new_event():
	return Event(1, 'Birthday', '2022-12-12', '18:00', 'Hawaiian', 'Blue and White')

def test_create_event(client, new_event):
	resp = client.post('/event', json=new_event.__dict__)
	assert resp.status_code == 201
	assert resp.get_json() == new_event.__dict__

	# Test creating an event with the same id
	resp = client.post('/event', json=new_event.__dict__)
	assert resp.status_code == 400
	assert resp.get_json() == {'message': 'Event with the same id already exists'}

def test_update_event(client, new_event):
	client.post('/event', json=new_event.__dict__)
	update = {'theme': 'Pirate', 'color_scheme': 'Black and White'}
	resp = client.put(f'/event/{new_event.id}', json=update)
	assert resp.status_code == 200
	assert resp.get_json()['theme'] == 'Pirate'
	assert resp.get_json()['color_scheme'] == 'Black and White'

	# Test updating an event that does not exist
	resp = client.put('/event/999', json=update)
	assert resp.status_code == 404
	assert resp.get_json() == {'message': 'Event not found'}
