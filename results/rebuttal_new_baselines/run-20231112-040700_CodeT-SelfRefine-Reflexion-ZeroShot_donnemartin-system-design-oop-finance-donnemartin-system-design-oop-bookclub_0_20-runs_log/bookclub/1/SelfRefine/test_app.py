import pytest
import app
from app import User, Club

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_user():
	return User(name='test_user', email='test@test.com', clubs=[])

@pytest.fixture
def sample_club():
	return Club(name='test_club', description='A test club', is_private=False, members=[])


def test_create_user(client, sample_user):
	response = client.post('/create_user', json=sample_user.__dict__)
	assert response.status_code == 201
	assert app.users.get('test_user') == sample_user


def test_create_club(client, sample_club):
	response = client.post('/create_club', json=sample_club.__dict__)
	assert response.status_code == 201
	assert app.clubs.get('test_club') == sample_club


def test_join_club(client, sample_user, sample_club):
	app.users[sample_user.name] = sample_user
	app.clubs[sample_club.name] = sample_club
	response = client.post('/join_club', json={'user_name': 'test_user', 'club_name': 'test_club'})
	assert response.status_code == 200
	assert sample_user in sample_club.members
	assert sample_club in sample_user.clubs


def test_create_existing_user(client, sample_user):
	app.users[sample_user.name] = sample_user
	response = client.post('/create_user', json=sample_user.__dict__)
	assert response.status_code == 400


def test_create_existing_club(client, sample_club):
	app.clubs[sample_club.name] = sample_club
	response = client.post('/create_club', json=sample_club.__dict__)
	assert response.status_code == 400


def test_join_existing_club(client, sample_user, sample_club):
	app.users[sample_user.name] = sample_user
	app.clubs[sample_club.name] = sample_club
	app.clubs[sample_club.name].members.append(sample_user)
	response = client.post('/join_club', json={'user_name': 'test_user', 'club_name': 'test_club'})
	assert response.status_code == 400
