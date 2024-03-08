import pytest
import app
from models import User, Club, Book, Meeting, Review

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/users', json={'id': '1', 'name': 'John Doe', 'email': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}


def test_create_club(client):
	response = client.post('/clubs', json={'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}


def test_create_book(client):
	response = client.post('/books', json={'id': '1', 'title': 'Book Title', 'author': 'Author Name', 'summary': 'Book Summary'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}


def test_create_meeting(client):
	response = client.post('/meetings', json={'id': '1', 'club_id': '1', 'book_id': '1', 'scheduled_time': '2022-01-01T00:00:00Z'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}


def test_create_review(client):
	response = client.post('/reviews', json={'id': '1', 'book_id': '1', 'user_id': '1', 'content': 'Great book!'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}

