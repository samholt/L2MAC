import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_meeting(client):
	response = client.post('/meeting', json={'id': '1', 'date_time': '2022-12-12 12:00', 'book_club_id': '1', 'attendees': ['1', '2']})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Meeting created successfully'}


def test_get_meeting(client):
	response = client.get('/meeting/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'date_time': '2022-12-12 12:00', 'book_club_id': '1', 'attendees': ['1', '2']}


def test_update_meeting(client):
	response = client.put('/meeting/1', json={'date_time': '2022-12-13 13:00'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Meeting updated successfully'}


def test_delete_meeting(client):
	response = client.delete('/meeting/1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Meeting deleted successfully'}
