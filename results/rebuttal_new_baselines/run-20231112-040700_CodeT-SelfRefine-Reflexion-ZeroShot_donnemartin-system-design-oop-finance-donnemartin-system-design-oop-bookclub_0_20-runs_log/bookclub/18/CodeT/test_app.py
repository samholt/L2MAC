import pytest
import app
from app import User, Club, Book, Meeting, Discussion, Resource

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_database():
	app.DATABASE = {
		'users': {},
		'clubs': {},
		'books': {},
		'meetings': {},
		'discussions': {},
		'resources': {}
	}

def test_create_user(client, reset_database):
	response = client.post('/users', json={
		'id': '1',
		'name': 'John Doe',
		'email': 'john.doe@example.com',
		'clubs': [],
		'books_read': [],
		'wish_list': [],
		'follows': []
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'John Doe',
		'email': 'john.doe@example.com',
		'clubs': [],
		'books_read': [],
		'wish_list': [],
		'follows': []
	}

# Similar tests for creating club, book, meeting, discussion, and resource
