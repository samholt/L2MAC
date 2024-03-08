import pytest
import auth
import database

@pytest.fixture
def client():
	with auth.app.test_client() as client:
		yield client


def test_register(client):
	database.users_db = {}
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert 'test' in database.users_db


def test_login(client):
	database.users_db = {'test': {'username': 'test', 'email': 'test@test.com', 'password': '$pbkdf2-sha256$29000$yIyK6C2erAkF4jlIqMd8ag$2dKy7iSie7G6xMbV8WeP9.KPa3GxZIS/.f/.6g/.6g'}}
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()

