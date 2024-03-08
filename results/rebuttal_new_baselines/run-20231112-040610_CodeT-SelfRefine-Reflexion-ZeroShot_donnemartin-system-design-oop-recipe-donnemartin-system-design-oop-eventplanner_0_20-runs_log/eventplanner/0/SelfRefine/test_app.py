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
	with app.app.app_context():
		app.Event.query.delete()
		app.db.session.commit()

@pytest.mark.usefixtures('reset_db')
def test_create_event(client):
	response = client.post('/event', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Event created'}
	assert app.Event.query.count() == 1
	assert app.Event.query.first().type == 'Birthday'

@pytest.mark.usefixtures('reset_db')
def test_update_event(client):
	event = app.Event(id=1, type='Birthday', date='2022-12-12', 'time': '18:00', theme='Space', color_scheme='Blue')
	app.db.session.add(event)
	app.db.session.commit()
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Event updated'}
	assert app.Event.query.count() == 1
	assert app.Event.query.first().type == 'Wedding'

@pytest.mark.usefixtures('reset_db')
def test_update_event_not_found(client):
	response = client.put('/event/1', json={'type': 'Wedding'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Event not found'}
