import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': 1, 'username': 'test', 'email': 'test@test.com', 'password': 'test', 'bio': '', 'website': '', 'location': '', 'is_private': False})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'username': 'test', 'email': 'test@test.com', 'password': 'test', 'bio': '', 'website': '', 'location': '', 'is_private': False}


def test_edit_profile(client):
	response = client.put('/edit_profile', json={'id': 1, 'bio': 'Test bio', 'website': 'https://test.com', 'location': 'Test location', 'is_private': True})
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'username': 'test', 'email': 'test@test.com', 'password': 'test', 'bio': 'Test bio', 'website': 'https://test.com', 'location': 'Test location', 'is_private': True}


def test_create_post(client):
	response = client.post('/create_post', json={'id': 1, 'user_id': 1, 'content': 'Test post', 'image_url': ''})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'user_id': 1, 'content': 'Test post', 'image_url': ''}


def test_delete_post(client):
	response = client.delete('/delete_post', json={'id': 1})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post deleted'}
