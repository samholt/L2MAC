import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert b'User registered successfully' in response.data


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert b'Logged in successfully' in response.data


def test_post(client):
	response = client.post('/post', json={'user_id': 1, 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert b'Post created successfully' in response.data


def test_like(client):
	response = client.post('/like', json={'post_id': 1})
	assert response.status_code == 200
	assert b'Post liked' in response.data


def test_retweet(client):
	response = client.post('/retweet', json={'post_id': 1})
	assert response.status_code == 200
	assert b'Post retweeted' in response.data


def test_reply(client):
	response = client.post('/reply', json={'post_id': 1, 'reply': 'Nice post!'})
	assert response.status_code == 200
	assert b'Reply added' in response.data
