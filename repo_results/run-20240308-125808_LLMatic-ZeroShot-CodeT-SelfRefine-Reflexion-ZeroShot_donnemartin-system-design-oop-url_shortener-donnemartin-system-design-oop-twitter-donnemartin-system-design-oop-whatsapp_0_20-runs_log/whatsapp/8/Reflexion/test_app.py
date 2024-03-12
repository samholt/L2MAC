import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}
	assert 'test@example.com' in app.users


def test_join_chat(client):
	app.chats['Test Chat'] = app.Chat('Test Chat', [])
	response = client.post('/join_chat', json={'chat_name': 'Test Chat', 'user_email': 'test@example.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User joined chat successfully'}
	assert 'test@example.com' in app.chats['Test Chat'].members


def test_leave_chat(client):
	app.chats['Test Chat'] = app.Chat('Test Chat', ['test@example.com'])
	response = client.post('/leave_chat', json={'chat_name': 'Test Chat', 'user_email': 'test@example.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User left chat successfully'}
	assert 'test@example.com' not in app.chats['Test Chat'].members
