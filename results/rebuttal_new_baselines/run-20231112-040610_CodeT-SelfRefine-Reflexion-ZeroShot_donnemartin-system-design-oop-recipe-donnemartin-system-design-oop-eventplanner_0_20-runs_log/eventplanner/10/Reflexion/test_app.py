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
	return Event(1, 'Birthday', '2022-12-12', '18:00', 'Hawaiian', 'Blue and White')


def test_create_event(client, event):
	response = client.post('/event', json=event.__dict__)
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}


def test_update_event(client, event):
	app.DB[1] = event
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Event updated'}
	assert app.DB[1].type == 'Wedding'


def test_update_event_not_found(client):
	response = client.put('/event/999', json={'type': 'Wedding'})
	assert response.status_code == 404
	assert response.get_json() == {'error': 'Event not found'}
