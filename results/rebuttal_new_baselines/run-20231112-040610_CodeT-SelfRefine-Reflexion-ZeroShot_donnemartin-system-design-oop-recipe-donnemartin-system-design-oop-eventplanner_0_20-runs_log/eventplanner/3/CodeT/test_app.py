import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	data = {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Hawaiian', 'color_scheme': 'Blue and White'}
	response = client.post('/event', json=data)
	assert response.status_code == 201
	assert response.get_json() == data


def test_update_event(client):
	data = {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Hawaiian', 'color_scheme': 'Blue and White'}
	app.DB[1] = Event(**data)
	updated_data = {'id': 1, 'type': 'Wedding', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Hawaiian', 'color_scheme': 'Blue and White'}
	response = client.put('/event/1', json=updated_data)
	assert response.status_code == 200
	assert response.get_json() == updated_data
