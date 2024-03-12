import pytest
from flask import Flask, json
from app import app, users, posts

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': '1', 'username': 'test', 'password': 'test', 'email': 'test@test.com', 'profile_picture': 'test.jpg', 'bio': 'test bio', 'website_link': 'www.test.com', 'location': 'test location'})
	assert response.status_code == 201
	assert 'User registered successfully' in response.get_data(as_text=True)


def test_login(client):
	response = client.post('/login', json={'id': '1', 'password': 'test'})
	assert response.status_code == 200


def test_post(client):
	response = client.post('/post', json={'id': '1', 'user_id': '1', 'text': 'Hello World', 'image': 'test.jpg'})
	assert response.status_code == 201
	assert 'Post created successfully' in response.get_data(as_text=True)


def test_like(client):
	response = client.post('/like', json={'post_id': '1'})
	assert response.status_code == 200
	assert 'Post liked' in response.get_data(as_text=True)


def test_notifications(client):
	response = client.get('/notifications', query_string={'user_id': '1'})
	assert response.status_code == 200


def test_trending(client):
	response = client.get('/trending')
	assert response.status_code == 200

