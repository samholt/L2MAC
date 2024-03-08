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
	club = Club('Test Club', 'This is a test club', False, [])
	user = User('Test User', [])
	app.clubs['Test Club'] = club
	app.users['Test User'] = user


def test_create_club(client, setup_data):
	response = client.post('/create_club', json={'name': 'New Club', 'description': 'This is a new club', 'is_private': False})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Club created successfully'
	assert 'New Club' in app.clubs

	response = client.post('/create_club', json={'name': 'New Club', 'description': 'This is a new club', 'is_private': False})
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Club already exists'


def test_join_club(client, setup_data):
	response = client.post('/join_club', json={'club_name': 'Test Club', 'user_name': 'Test User'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Joined club successfully'
	assert app.users['Test User'] in app.clubs['Test Club'].members
	assert app.clubs['Test Club'] in app.users['Test User'].clubs

	response = client.post('/join_club', json={'club_name': 'Test Club', 'user_name': 'Test User'})
	assert response.status_code == 400
	assert response.get_json()['message'] == 'User is already a member of this club'


def test_get_clubs(client, setup_data):
	response = client.get('/clubs')
	assert response.status_code == 200
	assert len(response.get_json()) == 1


def test_get_users(client, setup_data):
	response = client.get('/users')
	assert response.status_code == 200
	assert len(response.get_json()) == 1
