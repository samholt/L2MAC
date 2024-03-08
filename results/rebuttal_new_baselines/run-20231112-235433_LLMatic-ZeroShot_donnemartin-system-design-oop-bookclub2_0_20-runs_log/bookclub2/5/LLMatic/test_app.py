import pytest
from flask.testing import FlaskClient
from app import app, users, bookclubs, meetings

@pytest.fixture

def client():
	with app.test_client() as client:
		yield client


def test_create_user(client: FlaskClient):
	response = client.post('/create_user', json={'id': '1', 'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert users['1'] == {'id': '1', 'username': 'test', 'email': 'test@test.com', 'password': 'test'}


def test_join_bookclub(client: FlaskClient):
	response = client.post('/join_bookclub', json={'id': '1', 'name': 'test', 'description': 'test', 'privacy_settings': 'public'})
	assert response.status_code == 201
	assert bookclubs['1'] == {'id': '1', 'name': 'test', 'description': 'test', 'privacy_settings': 'public'}


def test_schedule_meeting(client: FlaskClient):
	response = client.post('/schedule_meeting', json={'id': '1', 'bookclub_id': '1', 'date': '2022-01-01', 'time': '12:00', 'location': 'test'})
	assert response.status_code == 201
	assert meetings['1'] == {'id': '1', 'bookclub_id': '1', 'date': '2022-01-01', 'time': '12:00', 'location': 'test'}
