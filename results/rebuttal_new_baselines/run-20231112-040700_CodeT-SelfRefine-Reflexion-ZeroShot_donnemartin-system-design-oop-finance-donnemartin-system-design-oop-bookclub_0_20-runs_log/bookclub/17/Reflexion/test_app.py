import pytest
import app
from app import User, Club, Book, Meeting

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/users', json={'id': '1', 'name': 'John Doe', 'email': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'John Doe', 'email': 'john@example.com'}

def test_create_club(client):
	response = client.post('/clubs', json={'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False}

def test_create_book(client):
	response = client.post('/books', json={'id': '1', 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}

def test_create_meeting(client):
	response = client.post('/meetings', json={'id': '1', 'club_id': '1', 'book_id': '1', 'date': '2022-12-31'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'club_id': '1', 'book_id': '1', 'date': '2022-12-31'}
