import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	data = {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'}
	response = client.post('/event', json=data)
	assert response.status_code == 201
	assert response.get_json() == data


def test_update_event(client):
	data = {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'}
	client.post('/event', json=data)
	update_data = {'theme': 'Marvel'}
	response = client.put(f'/event/{data['id']}', json=update_data)
	assert response.status_code == 200
	data.update(update_data)
	assert response.get_json() == data
