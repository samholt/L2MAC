import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'John', 'email': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Club created successfully'}


def test_join_club(client):
	client.post('/create_user', json={'name': 'John', 'email': 'john@example.com'})
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False})
	response = client.post('/join_club', json={'user_name': 'John', 'club_name': 'Book Club'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User joined the club successfully'}


def test_join_club_non_existent_user_or_club(client):
	response = client.post('/join_club', json={'user_name': 'NonExistentUser', 'club_name': 'NonExistentClub'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User or club does not exist'}


def test_join_private_club(client):
	client.post('/create_user', json={'name': 'John', 'email': 'john@example.com'})
	client.post('/create_club', json={'name': 'Private Club', 'description': 'A private club', 'is_private': True})
	response = client.post('/join_club', json={'user_name': 'John', 'club_name': 'Private Club'})
	assert response.status_code == 403
	assert response.get_json() == {'message': 'Cannot join a private club'}
