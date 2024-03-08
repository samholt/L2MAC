import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def event():
	return Event(id=1, type='Birthday', date='2022-12-12', time='18:00')


def test_create_event(client, event):
	response = client.post('/event', json=event.__dict__)
	assert response.status_code == 201
	assert app.DB[event.id] == event
