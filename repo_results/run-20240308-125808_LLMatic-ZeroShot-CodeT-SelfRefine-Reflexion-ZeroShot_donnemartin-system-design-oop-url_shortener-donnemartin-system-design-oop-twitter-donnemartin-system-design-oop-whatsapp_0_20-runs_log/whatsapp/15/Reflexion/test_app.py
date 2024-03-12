import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/users', json={'id': '1', 'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'email': 'test@test.com', 'password': 'password'}


def test_get_users(client):
	response = client.get('/users')
	assert response.status_code == 200
	assert response.get_json() == [{'id': '1', 'email': 'test@test.com', 'password': 'password'}]


def test_create_chat(client):
	response = client.post('/chats', json={'id': '1', 'users': ['1'], 'messages': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'users': ['1'], 'messages': []}


def test_get_user_chats(client):
	response = client.get('/users/1/chats')
	assert response.status_code == 200
	assert response.get_json() == [{'id': '1', 'users': ['1'], 'messages': []}]


def test_get_chat_messages(client):
	response = client.get('/chats/1/messages')
	assert response.status_code == 200
	assert response.get_json() == []
