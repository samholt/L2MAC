import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'Test User', 'email': 'test@example.com', 'books_read': [], 'books_to_read': [], 'clubs_joined': []})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Test Club', 'description': 'This is a test club', 'is_private': False, 'members': [], 'books': []})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Book club created successfully'}
