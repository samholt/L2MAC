import requests
import pytest

base_url = 'http://localhost:5000'

@pytest.fixture
def user():
	response = requests.post(f'{base_url}/register', json={
		'name': 'Test User',
		'email': 'test@example.com',
		'password': 'password'
	})
	return response.json()['user_id']


def test_profile(user):
	response = requests.get(f'{base_url}/profile?id={user}')
	assert response.status_code == 200
	data = response.json()
	assert data['name'] == 'Test User'
	assert data['email'] == 'test@example.com'
	assert data['profile_picture'] == ''
	assert data['storage_used'] == 0
