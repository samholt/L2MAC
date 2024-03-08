import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	event = Event(id=1, type='Birthday', date='2022-12-12', time='18:00', theme='Space', color_scheme='Blue')
	response = client.post('/event', json=event.__dict__)
	assert response.status_code == 201
	assert response.get_json() == event.__dict__


def test_get_event(client):
	event = Event(id=1, type='Birthday', date='2022-12-12', time='18:00', theme='Space', color_scheme='Blue')
	app.DB['event'] = event
	response = client.get('/event')
	assert response.status_code == 200
	assert response.get_json() == event.__dict__


def test_get_event_not_found(client):
	response = client.get('/event')
	assert response.status_code == 404
