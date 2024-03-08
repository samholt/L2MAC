import pytest
from app import app, DATABASE
from werkzeug.security import check_password_hash


def test_home():
	with app.test_client() as c:
		response = c.get('/')
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Welcome to the application!'}


def test_database():
	assert isinstance(DATABASE, dict)
	assert 'users' in DATABASE
	assert 'clubs' in DATABASE
	assert 'meetings' in DATABASE
	assert 'discussions' in DATABASE
	assert 'user_profiles' in DATABASE


def test_register():
	with app.test_client() as c:
		response = c.post('/register', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'User registered successfully'}
		assert 'test' in DATABASE['users']
		assert check_password_hash(DATABASE['users']['test'], 'test')


def test_login():
	with app.test_client() as c:
		response = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Logged in successfully'}


def test_create_club():
	with app.test_client() as c:
		response = c.post('/create_club', json={'club_name': 'book club', 'description': 'a club for book lovers', 'privacy': 'public'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Club created successfully'}
		assert 'book club' in DATABASE['clubs']
		assert DATABASE['clubs']['book club'] == {'description': 'a club for book lovers', 'privacy': 'public', 'members': {}}


def test_join_club():
	with app.test_client() as c:
		response = c.post('/join_club', json={'club_name': 'book club', 'username': 'test'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'User joined the club successfully'}
		assert 'test' in DATABASE['clubs']['book club']['members']
		assert DATABASE['clubs']['book club']['members']['test'] == 'member'


def test_manage_roles():
	with app.test_client() as c:
		response = c.post('/manage_roles', json={'club_name': 'book club', 'username': 'test', 'role': 'admin'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Role updated successfully'}
		assert DATABASE['clubs']['book club']['members']['test'] == 'admin'

