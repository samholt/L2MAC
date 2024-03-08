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

@pytest.mark.usefixtures('reset_db')
def test_create_event(client):
	data = {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}
	response = client.post('/event', json=data)
	assert response.status_code == 201
	assert response.get_json() == data

@pytest.mark.usefixtures('reset_db')
def test_update_event(client):
	data = {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}
	client.post('/event', json=data)
	update_data = {'type': 'Wedding'}
	response = client.put('/event/1', json=update_data)
	assert response.status_code == 200
	assert response.get_json()['type'] == 'Wedding'

@pytest.mark.usefixtures('reset_db')
def test_update_event_not_found(client):
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 404
