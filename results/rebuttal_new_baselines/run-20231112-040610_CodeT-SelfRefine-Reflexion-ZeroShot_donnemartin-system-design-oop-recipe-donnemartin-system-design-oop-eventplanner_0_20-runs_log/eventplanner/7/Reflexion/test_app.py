import pytest
import app

@pytest.fixture(autouse=True)
def reset_db():
	# Reset the DB before each test
	app.DB = {}

@pytest.mark.parametrize('event', [
	{'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'},
	{'id': 2, 'type': 'Wedding', 'date': '2023-01-01', 'time': '12:00', 'theme': 'Garden', 'color_scheme': 'Green'}
])
def test_create_event(client, event):
	response = client.post('/event', json=event)
	assert response.status_code == 201
	assert response.json == {'message': 'Event created', 'event': event}

@pytest.mark.parametrize('event_id', [1, 2])
def test_get_event(client, event_id):
	response = client.get(f'/event/{event_id}')
	assert response.status_code == 200
	assert response.json == {'event': app.DB[event_id].__dict__}

@pytest.mark.parametrize('event_id', [1, 2])
def test_delete_event(client, event_id):
	response = client.delete(f'/event/{event_id}')
	assert response.status_code == 200
	assert response.json == {'message': 'Event deleted'}
	assert event_id not in app.DB

def test_get_events(client):
	response = client.get('/events')
	assert response.status_code == 200
	assert set(event['id'] for event in response.json['events']) == set(app.DB.keys())
