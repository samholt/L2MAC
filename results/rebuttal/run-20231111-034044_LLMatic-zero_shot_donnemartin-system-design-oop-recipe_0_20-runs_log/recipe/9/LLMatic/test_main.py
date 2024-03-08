import pytest
from main import app
from flask import json

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Hello, World!'


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert 'username' in json.loads(response.data)
	assert 'password' in json.loads(response.data)


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'username' in json.loads(response.data)
	assert 'password' in json.loads(response.data)


def test_create_recipe(client):
	response = client.post('/recipe', json={'name': 'test', 'ingredients': ['test'], 'instructions': 'test', 'images': ['test'], 'categories': ['test'], 'user': 'test'})
	assert response.status_code == 201
	assert 'name' in json.loads(response.data)
	assert 'ingredients' in json.loads(response.data)
	assert 'instructions' in json.loads(response.data)
	assert 'images' in json.loads(response.data)
	assert 'categories' in json.loads(response.data)
	assert 'user' in json.loads(response.data)


def test_post_review(client):
	response = client.post('/review', json={'user': 'test', 'recipe': 'test', 'rating': 5, 'review_text': 'test'})
	assert response.status_code == 201
	assert 'user' in json.loads(response.data)
	assert 'recipe' in json.loads(response.data)
	assert 'rating' in json.loads(response.data)
	assert 'review_text' in json.loads(response.data)


def test_search(client):
	response = client.get('/search', query_string={'query': 'test'})
	assert response.status_code == 200


def test_admin_action(client):
	response = client.post('/admin', json={'action': 'test'})
	assert response.status_code == 204


def test_view_feed(client):
	response = client.get('/feed')
	assert response.status_code == 200


def test_get_recommendation(client):
	response = client.get('/recommendation')
	assert response.status_code == 200
