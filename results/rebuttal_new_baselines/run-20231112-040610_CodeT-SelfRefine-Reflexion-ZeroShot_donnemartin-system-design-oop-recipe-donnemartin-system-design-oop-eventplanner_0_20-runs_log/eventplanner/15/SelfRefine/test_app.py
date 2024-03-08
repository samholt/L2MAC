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
	return {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Nautical', 'color_scheme': 'Blue and White'}


def test_create_event(client, sample_event):
	response = client.post('/event', json=sample_event)
	assert response.status_code == 201
	assert Event.query.get(1).to_dict() == sample_event


def test_update_event(client, sample_event):
	event = Event(**sample_event)
	app.db.session.add(event)
	app.db.session.commit()
	response = client.put('/event/1', json={'theme': 'Space'})
	assert response.status_code == 200
	assert Event.query.get(1).theme == 'Space'
