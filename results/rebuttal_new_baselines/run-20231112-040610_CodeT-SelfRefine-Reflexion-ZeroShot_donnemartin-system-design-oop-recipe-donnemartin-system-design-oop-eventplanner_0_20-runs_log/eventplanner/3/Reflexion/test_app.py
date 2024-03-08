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
	return Event(id=1, type='Birthday', date='2022-12-12', time='18:00', theme='Hawaiian', color_scheme='Blue and White')


def test_create_event(client, sample_event):
	response = client.post('/event', json=sample_event.__dict__)
	assert response.status_code == 201
	assert response.get_json() == sample_event.__dict__


def test_get_event(client, sample_event):
	app.DATABASE[sample_event.id] = sample_event
	response = client.get(f'/event/{sample_event.id}')
	assert response.status_code == 200
	assert response.get_json() == sample_event.__dict__


def test_update_event(client, sample_event):
	app.DATABASE[sample_event.id] = sample_event
	update_data = {'theme': 'Space'}
	response = client.put(f'/event/{sample_event.id}', json=update_data)
	assert response.status_code == 200
	assert response.get_json()['theme'] == 'Space'


def test_delete_event(client, sample_event):
	app.DATABASE[sample_event.id] = sample_event
	response = client.delete(f'/event/{sample_event.id}')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Event deleted'}
	assert sample_event.id not in app.DATABASE
