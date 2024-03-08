import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_event():
	return Event(id=1, type='Birthday', date='2022-12-12', time='18:00', theme='Space', color_scheme='Blue')


def test_create_event(client, sample_event):
	response = client.post('/event', json=sample_event.__dict__)
	assert response.status_code == 201
	assert app.DB[1] == sample_event


def test_update_event(client, sample_event):
	app.DB[1] = sample_event
	response = client.put('/event/1', json={'theme': 'Pirate'})
	assert response.status_code == 200
	assert app.DB[1].theme == 'Pirate'
