import pytest
from app import app
from models import User, Club, Book

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

# User tests
def test_create_user(client):
	response = client.post('/user', json={'id': 1, 'name': 'Test User', 'email': 'test@example.com', 'books_read': [], 'clubs_joined': [], 'interests': []})
	assert response.status_code == 201

def test_get_user(client):
	response = client.get('/user/1')
	assert response.status_code == 200

def test_update_user(client):
	response = client.put('/user/1', json={'name': 'Updated User'})
	assert response.status_code == 200

def test_delete_user(client):
	response = client.delete('/user/1')
	assert response.status_code == 200

# Club tests
def test_create_club(client):
	response = client.post('/club', json={'id': 1, 'name': 'Test Club', 'description': 'This is a test club', 'members': [], 'books': [], 'meetings': [], 'is_private': False})
	assert response.status_code == 201

def test_get_club(client):
	response = client.get('/club/1')
	assert response.status_code == 200

def test_update_club(client):
	response = client.put('/club/1', json={'name': 'Updated Club'})
	assert response.status_code == 200

def test_delete_club(client):
	response = client.delete('/club/1')
	assert response.status_code == 200

# Book tests
def test_create_book(client):
	response = client.post('/book', json={'id': 1, 'title': 'Test Book', 'author': 'Test Author', 'summary': 'This is a test book', 'votes': 0})
	assert response.status_code == 201

def test_get_book(client):
	response = client.get('/book/1')
	assert response.status_code == 200

def test_update_book(client):
	response = client.put('/book/1', json={'title': 'Updated Book'})
	assert response.status_code == 200

def test_delete_book(client):
	response = client.delete('/book/1')
	assert response.status_code == 200

