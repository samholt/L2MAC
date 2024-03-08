import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	response = client.post('/event', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'}


def test_get_event(client):
	app.DB[1] = Event(1, 'Birthday', '2022-12-12', '18:00', 'Disney', 'Blue')
	response = client.get('/event/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'}


def test_get_event_not_found(client):
	response = client.get('/event/100')
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Event not found'}
