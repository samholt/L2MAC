import pytest
import app
from app import User, Club, Book, Discussion

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/user', json={
		'id': '1',
		'name': 'Test User',
		'email': 'test@example.com',
		'clubs': [],
		'books_read': [],
		'wish_list': []
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'Test User',
		'email': 'test@example.com',
		'clubs': [],
		'books_read': [],
		'wish_list': []
	}

def test_create_club(client):
	response = client.post('/club', json={
		'id': '1',
		'name': 'Test Club',
		'description': 'This is a test club.',
		'members': [],
		'books': [],
		'meetings': []
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'Test Club',
		'description': 'This is a test club.',
		'members': [],
		'books': [],
		'meetings': []
	}

def test_create_book(client):
	response = client.post('/book', json={
		'id': '1',
		'title': 'Test Book',
		'author': 'Test Author',
		'description': 'This is a test book.'
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'title': 'Test Book',
		'author': 'Test Author',
		'description': 'This is a test book.'
	}

def test_create_discussion(client):
	response = client.post('/discussion', json={
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'comments': []
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'comments': []
	}
