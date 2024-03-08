import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Club created successfully'}


def test_join_club(client):
	client.post('/create_user', json={'name': 'John Doe', 'email': 'john@example.com'})
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False})
	response = client.post('/join_club', json={'user_name': 'John Doe', 'club_name': 'Book Club'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User joined club successfully'}


def test_join_club_not_found(client):
	response = client.post('/join_club', json={'user_name': 'Nonexistent User', 'club_name': 'Nonexistent Club'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User or club not found'}
