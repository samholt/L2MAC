import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert 'id' in response.get_json()


def test_create_club(client):
	response = client.post('/book_clubs', json={'name': 'Test Club', 'description': 'A test book club', 'privacy': 'public'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_schedule_meeting(client):
	response = client.post('/book_clubs', json={'name': 'Test Club', 'description': 'A test book club', 'privacy': 'public'})
	assert response.status_code == 201
	book_club_id = response.get_json()['id']
	response = client.post('/meetings', json={'date': '2022-12-31', 'time': '12:00', 'book_club_id': book_club_id})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_create_discussion(client):
	response = client.post('/book_clubs', json={'name': 'Test Club', 'description': 'A test book club', 'privacy': 'public'})
	assert response.status_code == 201
	book_club_id = response.get_json()['id']
	response = client.post('/discussions', json={'topic': 'Test Discussion', 'book_club_id': book_club_id})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_add_book(client):
	response = client.post('/books', json={'title': 'Test Book', 'author': 'Test Author'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_create_notification(client):
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	user_id = response.get_json()['id']
	response = client.post('/notifications', json={'user_id': user_id, 'message': 'Test Notification'})
	assert response.status_code == 201
	assert 'id' in response.get_json()

