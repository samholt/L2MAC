import pytest
import app
from app import Club, User

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_club():
	return Club('Test Club', 'This is a test club', False, [])

@pytest.fixture
def sample_user():
	return User('Test User', [])


def test_create_club(client, sample_club):
	response = client.post('/create_club', json=sample_club.__dict__)
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Club created successfully'


def test_join_club(client, sample_club, sample_user):
	app.clubs[sample_club.name] = sample_club
	response = client.post('/join_club', json={'club_name': sample_club.name, 'user_name': sample_user.name})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Joined club successfully'
	assert sample_user in sample_club.members
	assert sample_club in sample_user.clubs
