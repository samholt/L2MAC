import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def init_db():
	with app.app.app_context():
		app.db.create_all()
		event = Event(id=1, type='Birthday', date='2022-12-12', time='18:00', theme='Nautical', color_scheme='Blue and White')
		app.db.session.add(event)
		app.db.session.commit()
		yield app.db
		app.db.drop_all()


def test_create_event(client, init_db):
	response = client.post('/create_event', json={'id': 2, 'type': 'Wedding', 'date': '2023-06-15', 'time': '12:00', 'theme': 'Rustic', 'color_scheme': 'Green and Brown'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Event created successfully'}
	assert Event.query.count() == 2


def test_update_event(client, init_db):
	response = client.put('/update_event/1', json={'type': 'Anniversary', 'date': '2023-01-01', 'time': '20:00', 'theme': 'Vintage', 'color_scheme': 'Gold and Black'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Event updated successfully'}
	event = Event.query.get(1)
	assert event.type == 'Anniversary'
	assert event.date == '2023-01-01'
	assert event.time == '20:00'
	assert event.theme == 'Vintage'
	assert event.color_scheme == 'Gold and Black'


def test_update_event_not_found(client, init_db):
	response = client.put('/update_event/99', json={'type': 'Anniversary', 'date': '2023-01-01', 'time': '20:00', 'theme': 'Vintage', 'color_scheme': 'Gold and Black'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Event not found'}
