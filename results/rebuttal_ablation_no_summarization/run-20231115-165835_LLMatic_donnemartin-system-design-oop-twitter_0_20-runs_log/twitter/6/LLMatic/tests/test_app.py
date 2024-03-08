import pytest
from flask import json
from app import app as flask_app, User, Post, Follow, Message, Notification, mock_db
from datetime import datetime

@pytest.fixture
def app():
	return flask_app


def test_home(app):
	with app.test_client() as client:
		response = client.get('/')
		assert response.status_code == 200
		assert response.data == b'Hello, World!'


def test_register(app):
	with app.test_client() as client:
		response = client.post('/register', data=json.dumps({'email': 'test@test.com', 'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert 'User registered successfully' in response.get_data(as_text=True)
		assert isinstance(mock_db['users'].get('test'), User)


def test_login(app):
	with app.test_client() as client:
		response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert 'token' in response.get_data(as_text=True)


def test_profile(app):
	with app.test_client() as client:
		response = client.post('/profile', data=json.dumps({'username': 'test', 'profile_picture': 'test.jpg', 'bio': 'test bio', 'website_link': 'test.com', 'location': 'test location', 'privacy_setting': 'private'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Profile updated successfully' in response.get_data(as_text=True)
		user = mock_db['users'].get('test')
		assert user.profile_picture == 'test.jpg'
		assert user.bio == 'test bio'
		assert user.website_link == 'test.com'
		assert user.location == 'test location'
		assert user.privacy_setting == 'private'
		response = client.get('/profile?username=test')
		assert response.status_code == 200
		data = json.loads(response.get_data(as_text=True))
		assert data['username'] == 'test'
		assert data['profile_picture'] == 'test.jpg'
		assert data['bio'] == 'test bio'
		assert data['website_link'] == 'test.com'
		assert data['location'] == 'test location'
		assert data['privacy_setting'] == 'private'


def test_post(app):
	with app.test_client() as client:
		response = client.post('/post', data=json.dumps({'author': 'test', 'content': 'test content', 'image': 'test.jpg'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Post created successfully' in response.get_data(as_text=True)
		assert any(isinstance(post, Post) for post in mock_db['posts'].values())


def test_follow(app):
	with app.test_client() as client:
		response = client.post('/follow', data=json.dumps({'follower': 'test', 'followee': 'test2'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Followed successfully' in response.get_data(as_text=True)
		assert isinstance(mock_db['follows'].get('test'), Follow)


def test_message(app):
	with app.test_client() as client:
		response = client.post('/message', data=json.dumps({'sender': 'test', 'recipient': 'test2', 'content': 'Hello'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Message sent successfully' in response.get_data(as_text=True)
		assert isinstance(mock_db['messages'].get('test'), Message)


def test_notifications(app):
	with app.test_client() as client:
		response = client.post('/notifications', data=json.dumps({'recipient': 'test', 'type': 'like', 'related_user': 'test2', 'related_post': 'Hello'}), content_type='application/json')
		assert response.status_code == 200
		assert 'Notification created successfully' in response.get_data(as_text=True)
		assert isinstance(mock_db['notifications'].get('test'), Notification)
		response = client.get('/notifications?recipient=test')
		assert response.status_code == 200
		data = json.loads(response.get_data(as_text=True))
		assert data['recipient'] == 'test'
		assert data['type'] == 'like'
		assert data['related_user'] == 'test2'
		assert data['related_post'] == 'Hello'


def test_search(app):
	with app.test_client() as client:
		response = client.get('/search?q=test')
		assert response.status_code == 200
		data = json.loads(response.get_data(as_text=True))
		assert 'test' in data['users']
		assert 'test content' in data['posts']


def test_trending(app):
	with app.test_client() as client:
		response = client.get('/trending')
		assert response.status_code == 200
		data = json.loads(response.get_data(as_text=True))
		assert 'trending_topics' in data


def test_recommendations(app):
	with app.test_client() as client:
		response = client.get('/recommendations?username=test')
		assert response.status_code == 200
		data = json.loads(response.get_data(as_text=True))
		assert 'user_recommendations' in data


def test_reset_password(app):
	with app.test_client() as client:
		response = client.post('/reset_password', data=json.dumps({'email': 'test@test.com'}), content_type='application/json')
		assert response.status_code == 200
		assert 'token' in response.get_data(as_text=True)
		response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
		assert response.status_code == 200
		assert 'token' in response.get_data(as_text=True)
