import pytest
import app
from app import Club, User

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def setup_data():
	app.clubs = {}
	app.users = {}
	app.clubs['Test Club'] = Club('Test Club', 'This is a test club', False, [])
	app.users['Test User'] = User('Test User', [])


def test_create_club(client, setup_data):
	response = client.post('/create_club', json={'name': 'New Club', 'description': 'This is a new club', 'is_private': False})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Club created successfully'}
	assert 'New Club' in app.clubs


def test_create_user(client, setup_data):
	response = client.post('/create_user', json={'name': 'New User'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}
	assert 'New User' in app.users


def test_join_club(client, setup_data):
	response = client.post('/join_club', json={'club_name': 'Test Club', 'user_name': 'Test User'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User joined club successfully'}
	assert app.users['Test User'] in app.clubs['Test Club'].members
	assert app.clubs['Test Club'] in app.users['Test User'].clubs


def test_list_clubs(client, setup_data):
	response = client.get('/list_clubs')
	assert response.status_code == 200
	assert response.get_json() == {'clubs': ['Test Club']}


def test_list_user_clubs(client, setup_data):
	response = client.get('/list_user_clubs', query_string={'user_name': 'Test User'})
	assert response.status_code == 200
	assert response.get_json() == {'clubs': []}
