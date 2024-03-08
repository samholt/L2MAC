import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': '1', 'name': 'Test User'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'name': 'Test User', 'recipes': [], 'favorites': []}


def test_create_recipe(client):
	response = client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2'], 'reviews': []}


def test_update_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	response = client.put('/recipe/1', json={'name': 'Updated Recipe'})
	assert response.status_code == 200
	assert json.loads(response.data)['name'] == 'Updated Recipe'


def test_delete_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	response = client.delete('/recipe/1')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Recipe deleted'}


def test_search_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	response = client.get('/recipe/search?q=Test')
	assert response.status_code == 200
	assert len(json.loads(response.data)) == 1


def test_add_favorite(client):
	client.post('/user', json={'id': '1', 'name': 'Test User'})
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	response = client.post('/user/1/favorites', json={'recipe_id': '1'})
	assert response.status_code == 200
	assert '1' in json.loads(response.data)['favorites']


def test_get_user_recipes(client):
	client.post('/user', json={'id': '1', 'name': 'Test User'})
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	app.users['1'].recipes.append('1')
	response = client.get('/user/1/recipes')
	assert response.status_code == 200
	assert len(json.loads(response.data)) == 1


def test_add_review(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	response = client.post('/recipe/1/review', json={'review': 'Test Review'})
	assert response.status_code == 200
	assert 'Test Review' in json.loads(response.data)['reviews']
