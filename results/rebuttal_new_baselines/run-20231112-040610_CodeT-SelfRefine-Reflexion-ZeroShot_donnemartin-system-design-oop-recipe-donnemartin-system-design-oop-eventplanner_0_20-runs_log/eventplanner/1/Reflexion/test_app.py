import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def event():
	return Event(id=1, type='Birthday', date='2022-12-12', time='18:00', theme='Space', color_scheme='Blue')


def test_create_event(client, event):
	response = client.post('/event', json=event.__dict__)
	assert response.status_code == 201
	assert response.get_json() == event.__dict__


def test_update_event(client, event):
	app.DB[event.id] = event
	update_data = {'theme': 'Pirate', 'color_scheme': 'Red'}
	response = client.put(f'/event/{event.id}', json=update_data)
	assert response.status_code == 200
	for key, value in update_data.items():
		assert getattr(app.DB[event.id], key) == value


def test_update_event_not_found(client):
	response = client.put('/event/999', json={'theme': 'Pirate'})
	assert response.status_code == 404
