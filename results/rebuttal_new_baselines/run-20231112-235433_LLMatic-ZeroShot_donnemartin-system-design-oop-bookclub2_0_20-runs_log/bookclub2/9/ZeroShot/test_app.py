import pytest
import app
from app import User, Club, Meeting, Forum, Profile, Admin

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {
		'users': {},
		'clubs': {},
		'meetings': {},
		'forums': {},
		'profiles': {},
		'admins': {}
	}

@pytest.mark.usefixtures('reset_db')
def test_create_user(client):
	response = client.post('/create_user', json={'id': '1', 'name': 'John'})
	assert response.status_code == 201
	assert app.DB['users']['1'].name == 'John'

@pytest.mark.usefixtures('reset_db')
def test_create_club(client):
	client.post('/create_user', json={'id': '1', 'name': 'John'})
	response = client.post('/create_club', json={'id': '1', 'name': 'Book Club', 'privacy': 'public', 'creator_id': '1'})
	assert response.status_code == 201
	assert app.DB['clubs']['1'].name == 'Book Club'

@pytest.mark.usefixtures('reset_db')
def test_create_meeting(client):
	client.post('/create_user', json={'id': '1', 'name': 'John'})
	client.post('/create_club', json={'id': '1', 'name': 'Book Club', 'privacy': 'public', 'creator_id': '1'})
	response = client.post('/create_meeting', json={'id': '1', 'club_id': '1', 'date': '2022-12-31'})
	assert response.status_code == 201
	assert app.DB['meetings']['1'].date == '2022-12-31'

@pytest.mark.usefixtures('reset_db')
def test_create_forum(client):
	client.post('/create_user', json={'id': '1', 'name': 'John'})
	client.post('/create_club', json={'id': '1', 'name': 'Book Club', 'privacy': 'public', 'creator_id': '1'})
	response = client.post('/create_forum', json={'id': '1', 'club_id': '1'})
	assert response.status_code == 201
	assert app.DB['forums']['1'].club.name == 'Book Club'

@pytest.mark.usefixtures('reset_db')
def test_create_profile(client):
	client.post('/create_user', json={'id': '1', 'name': 'John'})
	response = client.post('/create_profile', json={'id': '1', 'user_id': '1', 'reading_list': {'book1': 'read', 'book2': 'unread'}})
	assert response.status_code == 201
	assert app.DB['profiles']['1'].reading_list['book1'] == 'read'

@pytest.mark.usefixtures('reset_db')
def test_create_admin(client):
	client.post('/create_user', json={'id': '1', 'name': 'John'})
	response = client.post('/create_admin', json={'id': '1', 'user_id': '1'})
	assert response.status_code == 201
	assert app.DB['admins']['1'].user.name == 'John'
