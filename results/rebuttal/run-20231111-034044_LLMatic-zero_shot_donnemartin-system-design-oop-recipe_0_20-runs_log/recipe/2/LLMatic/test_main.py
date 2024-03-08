import pytest
from main import app
from flask import json

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Login successful'}


def test_submit_recipe(client):
	response = client.post('/submit_recipe', json={'name': 'test', 'ingredients': ['test'], 'instructions': ['test'], 'images': ['test'], 'category': 'test', 'type': 'test', 'cuisine': 'test', 'diet': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Recipe submitted successfully'}


def test_search(client):
	response = client.get('/search', query_string={'search_term': 'test'})
	assert response.status_code == 200
	assert 'test' in json.loads(response.data)['results']


def test_rate(client):
	response = client.post('/rate', json={'username': 'test', 'recipe_name': 'test', 'rating': 5, 'review': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Rating submitted successfully'}


def test_recommend(client):
	response = client.get('/recommend', query_string={'username': 'test'})
	assert response.status_code == 200
	assert isinstance(json.loads(response.data)['recommended_recipes'], list)
