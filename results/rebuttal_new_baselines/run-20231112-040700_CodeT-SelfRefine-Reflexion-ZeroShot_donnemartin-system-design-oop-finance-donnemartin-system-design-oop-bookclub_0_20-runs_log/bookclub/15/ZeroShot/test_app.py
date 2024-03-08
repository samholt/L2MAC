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
	user = User('test_user', {})
	club = Club('test_club', 'A test club', False, {})
	app.users[user.name] = user
	app.clubs[club.name] = club


def test_create_club(client, setup_data):
	response = client.post('/create_club', json={'name': 'new_club', 'description': 'A new club', 'is_private': False, 'members': {}})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Club created successfully'
	assert 'new_club' in app.clubs


def test_join_club(client, setup_data):
	response = client.post('/join_club', json={'user_name': 'test_user', 'club_name': 'test_club'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Joined club successfully'
	assert 'test_user' in app.clubs['test_club'].members
	assert 'test_club' in app.users['test_user'].clubs
