import pytest
import json
from routes import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200


def test_reset_password(client):
	response = client.post('/reset_password', json={'username': 'test', 'password': 'test', 'new_password': 'test2'})
	assert response.status_code == 200


def test_edit_profile(client):
	response = client.post('/edit_profile', json={'username': 'test', 'new_username': 'test2'})
	assert response.status_code == 200


def test_create_post(client):
	response = client.post('/create_post', json={'username': 'test', 'post_content': 'Hello, World!'})
	assert response.status_code == 200


def test_delete_post(client):
	response = client.post('/delete_post', json={'username': 'test', 'post_id': 1})
	assert response.status_code == 200


def test_like_post(client):
	response = client.post('/like_post', json={'username': 'test', 'post_id': 1})
	assert response.status_code == 200


def test_create_comment(client):
	response = client.post('/create_comment', json={'username': 'test', 'post_id': 1, 'comment_content': 'Nice post!'})
	assert response.status_code == 200


def test_delete_comment(client):
	response = client.post('/delete_comment', json={'username': 'test', 'comment_id': 1})
	assert response.status_code == 200


def test_follow_user(client):
	response = client.post('/follow_user', json={'username': 'test', 'user_to_follow': 'test2'})
	assert response.status_code == 200


def test_unfollow_user(client):
	response = client.post('/unfollow_user', json={'username': 'test', 'user_to_unfollow': 'test2'})
	assert response.status_code == 200


def test_send_message(client):
	response = client.post('/send_message', json={'sender': 'test', 'receiver': 'test2', 'message_content': 'Hello!'})
	assert response.status_code == 200


def test_delete_message(client):
	response = client.post('/delete_message', json={'username': 'test', 'message_id': 1})
	assert response.status_code == 200


def test_view_notifications(client):
	response = client.get('/view_notifications')
	assert response.status_code == 200


def test_view_trending(client):
	response = client.get('/view_trending')
	assert response.status_code == 200
