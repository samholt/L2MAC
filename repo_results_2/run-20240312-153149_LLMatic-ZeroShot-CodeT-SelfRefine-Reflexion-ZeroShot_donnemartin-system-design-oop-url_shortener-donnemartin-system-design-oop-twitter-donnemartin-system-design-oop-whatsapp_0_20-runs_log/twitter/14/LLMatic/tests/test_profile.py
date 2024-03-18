import pytest
from models import User, users_db
from app import app


def setup_function():
	users_db.clear()
	users_db['testuser'] = User('testuser@test.com', 'testuser', 'testpassword')


def test_profile():
	with app.test_client() as client:
		response = client.get('/profile/testuser');
		assert response.status_code == 200
		assert response.get_json() == {'username': 'testuser', 'email': 'testuser@test.com', 'profile_picture': None, 'bio': None, 'website_link': None, 'location': None, 'following': [], 'followers': []}

		response = client.put('/profile/testuser', json={'password': 'testpassword', 'bio': 'updated bio'});
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Profile updated successfully'}
		assert users_db['testuser'].bio == 'updated bio'
