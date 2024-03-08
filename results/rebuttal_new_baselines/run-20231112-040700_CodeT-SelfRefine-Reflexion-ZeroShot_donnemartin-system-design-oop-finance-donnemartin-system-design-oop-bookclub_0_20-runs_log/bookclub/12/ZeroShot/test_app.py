import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('user', [
	{'id': '1', 'name': 'John Doe', 'email': 'john@example.com', 'clubs': [], 'books_read': [], 'books_to_read': []},
	{'id': '2', 'name': 'Jane Doe', 'email': 'jane@example.com', 'clubs': [], 'books_read': [], 'books_to_read': []}
])
def test_create_user(client, user):
	response = client.post('/user', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == user

@pytest.mark.parametrize('club', [
	{'id': '1', 'name': 'Book Club 1', 'description': 'A book club', 'is_private': False, 'members': [], 'books': []},
	{'id': '2', 'name': 'Book Club 2', 'description': 'Another book club', 'is_private': True, 'members': [], 'books': []}
])
def test_create_club(client, club):
	response = client.post('/club', data=json.dumps(club), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == club
