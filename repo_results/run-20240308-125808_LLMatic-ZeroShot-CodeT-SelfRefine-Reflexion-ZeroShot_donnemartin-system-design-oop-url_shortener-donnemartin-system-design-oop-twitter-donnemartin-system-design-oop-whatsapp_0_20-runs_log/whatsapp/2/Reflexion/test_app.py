import pytest
from app import app
from database import users, groups

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture(autouse=True)
def clear_data():
	users.clear()
	groups.clear()


def test_register(client):
	response = client.post('/register', json={'id': '1', 'name': 'John', 'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	client.post('/register', json={'id': '1', 'name': 'John', 'email': 'john@example.com', 'password': 'password'})
	response = client.post('/login', json={'id': '1', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_get_user(client):
	client.post('/register', json={'id': '1', 'name': 'John', 'email': 'john@example.com', 'password': 'password'})
	response = client.get('/user/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'name': 'John', 'email': 'john@example.com', 'password': 'password', 'profile_picture': '', 'status_message': '', 'contacts': [], 'groups': [], 'blocked_contacts': [], 'last_seen_status': 'everyone'}


def test_create_group(client):
	response = client.post('/group', json={'id': '1', 'name': 'Group 1'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Group created successfully'}


def test_get_group(client):
	client.post('/group', json={'id': '1', 'name': 'Group 1'})
	response = client.get('/group/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'name': 'Group 1', 'members': [], 'admins': [], 'group_picture': '', 'visible_to': []}
