import pytest
import app
from app import Book, Club, User

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_club(client):
	response = client.post('/club', json={'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers', 'books': [], 'members': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers', 'books': [], 'members': []}


def test_add_book_to_club(client):
	client.post('/club', json={'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers', 'books': [], 'members': []})
	response = client.post('/club/1/add_book', json={'id': '1', 'title': 'Book Title', 'author': 'Book Author', 'clubs': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'title': 'Book Title', 'author': 'Book Author', 'clubs': ['1']}


def test_create_user(client):
	response = client.post('/user', json={'id': '1', 'name': 'User Name', 'clubs': [], 'books': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'User Name', 'clubs': [], 'books': []}
