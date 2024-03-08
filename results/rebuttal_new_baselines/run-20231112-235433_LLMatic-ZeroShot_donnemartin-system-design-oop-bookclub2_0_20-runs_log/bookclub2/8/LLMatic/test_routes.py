import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_create_book_club(client):
	response = client.post('/book_club', json={'name': 'test', 'description': 'test', 'is_private': False})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Book club created successfully'}


def test_schedule_meeting(client):
	response = client.post('/meeting', json={'date': '2022-01-01', 'time': '12:00', 'book': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Meeting scheduled successfully'}


def test_create_forum(client):
	response = client.post('/forum', json={'book_club': 'test', 'book': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Forum created successfully'}


def test_create_profile(client):
	response = client.post('/profile', json={'username': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Profile created successfully'}


def test_create_admin(client):
	response = client.post('/admin', json={'username': 'test', 'managed_book_clubs': ['test']})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Admin created successfully'}
