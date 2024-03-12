import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		client.post('/signup', json={'email': 'test@test.com', 'password': 'test'})
		client.post('/signup', json={'email': 'member@test.com', 'password': 'test'})
		client.post('/signup', json={'email': 'admin@test.com', 'password': 'test'})
		client.post('/create_group', json={'group_name': 'test_group', 'admin_email': 'test@test.com'})
		yield client


def test_create_group(client):
	response = client.post('/create_group', json={'group_name': 'test_group_2', 'admin_email': 'test@test.com'})
	assert response.status_code == 201
	assert 'test_group_2' in app.DATABASE['groups']


def test_add_member(client):
	response = client.post('/add_member', json={'group_name': 'test_group', 'member_email': 'member@test.com'})
	assert response.status_code == 200
	assert 'member@test.com' in app.DATABASE['groups']['test_group']['members']


def test_remove_member(client):
	response = client.post('/remove_member', json={'group_name': 'test_group', 'member_email': 'member@test.com'})
	assert response.status_code == 200
	assert 'member@test.com' not in app.DATABASE['groups']['test_group']['members']


def test_add_admin(client):
	response = client.post('/add_admin', json={'group_name': 'test_group', 'admin_email': 'admin@test.com'})
	assert response.status_code == 200
	assert 'admin@test.com' in app.DATABASE['groups']['test_group']['admins']


def test_remove_admin(client):
	response = client.post('/remove_admin', json={'group_name': 'test_group', 'admin_email': 'admin@test.com'})
	assert response.status_code == 200
	assert 'admin@test.com' not in app.DATABASE['groups']['test_group']['admins']

