import pytest
from models import User, users_db
from app import app


def setup_function():
	users_db.clear()
	users_db['testuser'] = User('testuser@test.com', 'testuser', 'testpassword')
	users_db['testuser2'] = User('testuser2@test.com', 'testuser2', 'testpassword2')


def test_follow():
	with app.test_client() as client:
		response = client.post('/follow/testuser2', json={'username': 'testuser', 'password': 'testpassword'});
		assert response.status_code == 200
		assert response.get_json() == {'message': 'User followed successfully'}
		assert 'testuser2' in users_db['testuser'].following
		assert 'testuser' in users_db['testuser2'].followers
