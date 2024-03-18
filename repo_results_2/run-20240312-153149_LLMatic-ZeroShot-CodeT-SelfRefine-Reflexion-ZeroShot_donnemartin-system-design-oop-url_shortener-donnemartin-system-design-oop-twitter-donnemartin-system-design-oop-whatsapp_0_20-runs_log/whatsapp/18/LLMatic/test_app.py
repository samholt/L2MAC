import pytest
import app
import base64

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200


def test_register_page(client):
	response = client.get('/register')
	assert response.status_code == 200


def test_login_page(client):
	response = client.get('/login')
	assert response.status_code == 200


def test_profile_page(client):
	response = client.get('/profile/test_user')
	assert response.status_code == 404


def test_group_chat_page(client):
	response = client.get('/group_chat/test_group')
	assert response.status_code == 404


def test_status_page(client):
	response = client.get('/status/test_user')
	assert response.status_code == 404


def test_post_status(client):
	response = client.post('/post-status', json={'user_id': 'test_user', 'image': 'test_image'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Status posted successfully'


def test_update_status_visibility(client):
	response = client.post('/update-status-visibility', json={'user_id': 'test_user', 'visibility': 'public'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Status visibility updated successfully'
