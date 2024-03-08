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
	club = Club('test_club', 'A test club', False, [])
	app.users[user.name] = user
	app.clubs[club.name] = club


def test_create_club(client, setup_data):
	response = client.post('/create_club', json={'name': 'new_club', 'description': 'A new club', 'is_private': False, 'members': []})
	assert response.status_code == 201
	assert response.get_json()['name'] == 'new_club'


def test_join_club(client, setup_data):
	response = client.post('/join_club', json={'user_name': 'test_user', 'club_name': 'test_club'})
	assert response.status_code == 200
	assert 'test_user' in response.get_json()['members']


def test_create_existing_club(client, setup_data):
	response = client.post('/create_club', json={'name': 'test_club', 'description': 'A test club', 'is_private': False, 'members': []})
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_join_nonexistent_club(client, setup_data):
	response = client.post('/join_club', json={'user_name': 'test_user', 'club_name': 'nonexistent_club'})
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_join_club_already_member(client, setup_data):
	client.post('/join_club', json={'user_name': 'test_user', 'club_name': 'test_club'})
	response = client.post('/join_club', json={'user_name': 'test_user', 'club_name': 'test_club'})
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_leave_club(client, setup_data):
	client.post('/join_club', json={'user_name': 'test_user', 'club_name': 'test_club'})
	response = client.post('/leave_club', json={'user_name': 'test_user', 'club_name': 'test_club'})
	assert response.status_code == 200
	assert 'test_user' not in response.get_json()['members']
