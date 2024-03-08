import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com', 'books_read': [], 'books_to_read': [], 'clubs': []})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'members': [], 'books': [], 'meetings': []})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Book club created successfully'}


def test_join_club(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com', 'books_read': [], 'books_to_read': [], 'clubs': []})
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'members': [], 'books': [], 'meetings': []})
	response = client.post('/join_club', json={'user_email': 'john@example.com', 'club_name': 'Book Club'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User joined the club successfully'}


def test_add_book(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com', 'books_read': [], 'books_to_read': [], 'clubs': []})
	response = client.post('/add_book', json={'user_email': 'john@example.com', 'book': 'Moby Dick'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Book added to reading list successfully'}


def test_mark_book_as_read(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com', 'books_read': [], 'books_to_read': ['Moby Dick'], 'clubs': []})
	response = client.post('/mark_book_as_read', json={'user_email': 'john@example.com', 'book': 'Moby Dick'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Book marked as read successfully'}


def test_create_meeting(client):
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'members': [], 'books': [], 'meetings': []})
	response = client.post('/create_meeting', json={'club_name': 'Book Club', 'meeting': '2022-12-31'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Meeting created successfully'}
