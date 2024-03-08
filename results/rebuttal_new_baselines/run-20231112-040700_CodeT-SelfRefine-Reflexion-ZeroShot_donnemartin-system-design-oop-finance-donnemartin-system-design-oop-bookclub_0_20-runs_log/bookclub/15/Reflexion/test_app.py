import pytest
import app
from app import Club, User

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_club(client):
	response = client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Club created successfully'}
	assert isinstance(app.clubs['Book Club'], Club)

def test_create_user(client):
	response = client.post('/create_user', json={'name': 'John'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}
	assert isinstance(app.users['John'], User)

def test_join_club(client):
	client.post('/create_club', json={'name': 'Book Club', 'description': 'A club for book lovers', 'is_private': False})
	client.post('/create_user', json={'name': 'John'})
	response = client.post('/join_club', json={'club_name': 'Book Club', 'user_name': 'John'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User joined the club successfully'}
	assert 'John' in app.clubs['Book Club'].members
	assert 'Book Club' in app.users['John'].clubs
