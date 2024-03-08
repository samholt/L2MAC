import pytest
import main
from flask import Flask, request

@pytest.fixture
def client():
	main.app.config['TESTING'] = True
	with main.app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.data == b'Hello, World!'


def test_create_account(client):
	response = client.post('/create_account', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200


def test_submit_recipe(client):
	response = client.post('/submit_recipe', json={'id': '1', 'recipe': 'test recipe', 'category': 'test category', 'ingredients': 'test ingredients', 'instructions': 'test instructions', 'ratings': [], 'reviews': []})
	assert response.status_code == 200


def test_submit_review(client):
	response = client.post('/submit_review', json={'id': '1', 'user': 'test user', 'rating': 5, 'content': 'test content'})
	assert response.status_code == 200


def test_search(client):
	response = client.get('/search', query_string={'query': 'test'})
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)


def test_admin(client):
	response = client.post('/admin', json={'action': 'delete', 'target': 'test'})
	assert response.status_code == 200


def test_feed(client):
	response = client.get('/feed', query_string={'user_id': 'test'})
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)


def test_recommendation(client):
	response = client.get('/recommendation', query_string={'user_id': 'test'})
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)
