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
	app.DB = {}

@pytest.mark.usefixtures('reset_db')
def test_create_event(client):
	response = client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}

@pytest.mark.usefixtures('reset_db')
def test_update_event(client):
	client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'})
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Event updated'}
	assert app.DB[1].type == 'Wedding'

@pytest.mark.usefixtures('reset_db')
def test_update_event_not_found(client):
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 404
	assert response.get_json() == {'error': 'Event not found'}
