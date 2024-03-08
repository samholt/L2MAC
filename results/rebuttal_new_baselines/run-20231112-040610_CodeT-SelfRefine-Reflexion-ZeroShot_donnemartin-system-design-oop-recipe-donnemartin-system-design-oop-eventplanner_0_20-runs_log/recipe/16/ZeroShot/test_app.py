import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/user', json={'id': '1', 'name': 'Test User', 'recipes': [], 'favorites': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Test User', 'recipes': [], 'favorites': []}

def test_create_recipe(client):
	response = client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': [], 'instructions': [], 'images': [], 'categories': [], 'reviews': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Test Recipe', 'ingredients': [], 'instructions': [], 'images': [], 'categories': [], 'reviews': []}

def test_update_recipe(client):
	response = client.put('/recipe/1', json={'name': 'Updated Recipe'})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'Updated Recipe'

def test_delete_recipe(client):
	response = client.delete('/recipe/1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe deleted'}

def test_search_recipe(client):
	response = client.get('/recipe/search?query=Updated')
	assert response.status_code == 200
	assert len(response.get_json()) == 1

def test_add_favorite(client):
	response = client.post('/user/1/favorites', json={'recipe_id': '1'})
	assert response.status_code == 200
	assert len(response.get_json()['favorites']) == 1

def test_get_favorites(client):
	response = client.get('/user/1/favorites')
	assert response.status_code == 200
	assert len(response.get_json()) == 1

def test_add_review(client):
	response = client.post('/recipe/1/review', json={'user_id': '1', 'rating': 5, 'comment': 'Great recipe!'})
	assert response.status_code == 200
	assert len(response.get_json()['reviews']) == 1
