import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'id': '1', 'name': 'John Doe', 'email': 'john@example.com', 'clubs': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'John Doe', 'email': 'john@example.com', 'clubs': []}


def test_create_club(client):
	response = client.post('/create_club', json={'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'members': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False, 'members': []}
