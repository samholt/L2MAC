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
	return Event(id=1, type='Birthday', date='2022-12-12', time='18:00', theme='Nautical', color_scheme='Blue and White')


def test_create_event(client, sample_event):
	response = client.post('/event', json=sample_event.__dict__)
	assert response.status_code == 201
	assert app.DB[1] == sample_event


def test_get_event(client, sample_event):
	app.DB[1] = sample_event
	response = client.get('/event/1')
	assert response.status_code == 200
	assert response.get_json() == sample_event.__dict__


def test_get_event_not_found(client):
	response = client.get('/event/1')
	assert response.status_code == 404
