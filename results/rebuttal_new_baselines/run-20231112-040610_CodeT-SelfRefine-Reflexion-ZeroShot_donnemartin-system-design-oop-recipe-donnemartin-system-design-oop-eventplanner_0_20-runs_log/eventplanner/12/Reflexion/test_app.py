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
	app.DB['events'] = []

@pytest.mark.usefixtures('reset_db')
def test_create_event(client):
	response = client.post('/events', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}

@pytest.mark.usefixtures('reset_db')
def test_update_event(client):
	app.DB['events'].append(Event(1, 'Birthday', '2022-12-12', '18:00', 'Space', 'Blue'))
	response = client.put('/events/1', json={'theme': 'Pirate'})
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Pirate', 'color_scheme': 'Blue'}

@pytest.mark.usefixtures('reset_db')
def test_delete_event(client):
	app.DB['events'].append(Event(1, 'Birthday', '2022-12-12', '18:00', 'Space', 'Blue'))
	response = client.delete('/events/1')
	assert response.status_code == 204
	assert len(app.DB['events']) == 0
