import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Club created successfully'}


def test_join_club(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com'})
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers'})
	response = client.post('/join_club', json={'email': 'john@example.com', 'club_name': 'Book Club'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Joined club successfully'}


def test_add_book(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com'})
	response = client.post('/add_book', json={'email': 'john@example.com', 'book_name': 'Moby Dick'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Book added successfully'}
