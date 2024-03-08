import pytest
from app import app, DATABASE

def test_home():
	with app.test_client() as client:
		response = client.get('/')
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Welcome to the application!'}

def test_database():
	DATABASE['users']['test_user'] = {'password': 'test_password', 'clubs': []}
	assert DATABASE['users']['test_user']['password'] == 'test_password'

def test_register():
	with app.test_client() as client:
		response = client.post('/register', json={'username': 'test_user2', 'password': 'test_password2'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'User registered successfully'}
		assert 'test_user2' in DATABASE['users']
		assert DATABASE['users']['test_user2']['password'] == 'test_password2'

def test_login():
	with app.test_client() as client:
		response = client.post('/login', json={'username': 'test_user', 'password': 'test_password'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Logged in successfully'}

def test_create_club():
	with app.test_client() as client:
		response = client.post('/create_club', json={'club_name': 'test_club', 'privacy_setting': 'public', 'admin': 'test_user'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Club created successfully'}
		assert 'test_club' in DATABASE['clubs']
		assert DATABASE['clubs']['test_club']['privacy_setting'] == 'public'
		assert 'test_user' in DATABASE['clubs']['test_club']['members']
		assert 'test_user' in DATABASE['clubs']['test_club']['admins']

def test_join_club():
	with app.test_client() as client:
		response = client.post('/join_club', json={'club_name': 'test_club', 'username': 'test_user2'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Joined club successfully'}
		assert 'test_user2' in DATABASE['clubs']['test_club']['members']
		assert 'test_club' in DATABASE['users']['test_user2']['clubs']

def test_manage_roles():
	with app.test_client() as client:
		response = client.post('/manage_roles', json={'club_name': 'test_club', 'username': 'test_user2', 'role': 'admin', 'admin': 'test_user'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Role managed successfully'}
		assert 'test_user2' in DATABASE['clubs']['test_club']['admins']

def test_schedule_meeting():
	with app.test_client() as client:
		response = client.post('/schedule_meeting', json={'meeting_id': 'test_meeting', 'club_name': 'test_club', 'date_time': '2022-12-31 12:00:00', 'attendees': ['test_user', 'test_user2']})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Meeting scheduled successfully'}
		assert 'test_meeting' in DATABASE['meetings']
		assert DATABASE['meetings']['test_meeting']['club_name'] == 'test_club'
		assert DATABASE['meetings']['test_meeting']['date_time'] == '2022-12-31 12:00:00'
		assert 'test_user' in DATABASE['meetings']['test_meeting']['attendees']
		assert 'test_user2' in DATABASE['meetings']['test_meeting']['attendees']

