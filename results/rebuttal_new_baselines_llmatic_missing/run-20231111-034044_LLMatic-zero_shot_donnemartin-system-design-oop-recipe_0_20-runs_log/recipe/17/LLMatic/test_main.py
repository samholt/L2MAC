import pytest
import main
from flask import json

@pytest.fixture
def client():
	main.app.config['TESTING'] = True
	with main.app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Hello, World!'


def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_create_recipe(client):
	response = client.post('/recipe', json={'name': 'test', 'ingredients': ['test'], 'instructions': ['test'], 'images': ['test'], 'categories': ['test']})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Recipe created successfully'}


def test_search(client):
	response = client.get('/search?name=test')
	assert response.status_code == 200
	assert 'test' in json.loads(response.data)['results']


def test_rate(client):
	response = client.post('/rate', json={'user_id': 'test', 'recipe_id': 'test', 'rating': 5})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Recipe rated successfully'}


def test_review(client):
	response = client.post('/review', json={'user_id': 'test', 'recipe_id': 'test', 'review': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Review written successfully'}


def test_follow(client):
	response = client.post('/follow', json={'follower_id': 'test', 'followee_id': 'test2'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User followed successfully'}


def test_feed(client):
	response = client.get('/feed?user_id=test')
	assert response.status_code == 200


def test_admin(client):
	response = client.get('/admin')
	assert response.status_code == 200


def test_recommend(client):
	response = client.get('/recommend?user_id=test')
	assert response.status_code == 200
