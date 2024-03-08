import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {'events': []}

def test_create_event(client, reset_db):
	response = client.post('/event', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}

	assert len(app.DB['events']) == 1
	assert app.DB['events'][0] == Event(1, 'Birthday', '2022-12-12', '18:00', 'Space', 'Blue')


def test_update_event(client, reset_db):
	app.DB['events'].append(Event(1, 'Birthday', '2022-12-12', '18:00', 'Space', 'Blue'))
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'type': 'Wedding', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}

	assert len(app.DB['events']) == 1
	assert app.DB['events'][0] == Event(1, 'Wedding', '2022-12-12', '18:00', 'Space', 'Blue')


def test_update_event_not_found(client, reset_db):
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 404
	assert response.get_json() == {'error': 'Event not found'}
