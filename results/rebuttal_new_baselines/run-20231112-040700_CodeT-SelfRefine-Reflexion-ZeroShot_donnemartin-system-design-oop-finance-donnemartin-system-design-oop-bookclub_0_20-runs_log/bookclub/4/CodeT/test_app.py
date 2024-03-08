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
	user = User('test_user', [])
	app.users['test_user'] = user
	club = Club('test_club', 'This is a test club', False, [])
	app.clubs['test_club'] = club

@pytest.mark.parametrize('club_name, description, is_private', [('test_club', 'This is a test club', False)])
def test_create_club(client, club_name, description, is_private):
	response = client.post('/create_club', json={'name': club_name, 'description': description, 'is_private': is_private})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Club created successfully'}

@pytest.mark.parametrize('club_name, user_name', [('test_club', 'test_user')])
def test_join_club(client, setup_data, club_name, user_name):
	response = client.post('/join_club', json={'club_name': club_name, 'user_name': user_name})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Joined club successfully'}
