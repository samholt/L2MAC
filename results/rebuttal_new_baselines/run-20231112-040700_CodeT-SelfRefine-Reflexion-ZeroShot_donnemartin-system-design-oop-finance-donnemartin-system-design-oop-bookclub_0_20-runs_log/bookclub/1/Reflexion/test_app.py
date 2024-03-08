import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': 1, 'name': 'Test User', 'email': 'test@example.com', 'clubs': [], 'books': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'name': 'Test User', 'email': 'test@example.com', 'clubs': [], 'books': []}


def test_create_club(client):
	response = client.post('/club', json={'id': 1, 'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': [], 'books': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': [], 'books': []}


def test_create_book(client):
	response = client.post('/book', json={'id': 1, 'title': 'Test Book', 'author': 'Test Author', 'description': 'This is a test book'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'title': 'Test Book', 'author': 'Test Author', 'description': 'This is a test book'}
