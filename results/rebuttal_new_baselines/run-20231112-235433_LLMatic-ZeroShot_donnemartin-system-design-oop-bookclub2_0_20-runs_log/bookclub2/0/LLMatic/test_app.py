import pytest
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_create_book_club(client):
	response = client.post('/book_clubs', json={'name': 'test', 'privacy_settings': 'public', 'admin': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Book club created successfully'}


def test_schedule_meeting(client):
	response = client.post('/meetings', json={'date': '2022-12-31', 'time': '12:00', 'book_club': 'test', 'attendees': ['test']})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Meeting scheduled successfully'}


def test_create_discussion(client):
	response = client.post('/discussions', json={'book_club': 'test', 'topic': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Discussion created successfully'}


def test_create_admin(client):
	response = client.post('/admins', json={'user': 'test', 'dashboard': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Admin created successfully'}
