import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/users', json={'id': '1', 'name': 'Test User', 'recipes': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Test User', 'recipes': []}

def test_get_user(client):
	response = client.get('/users/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'name': 'Test User', 'recipes': []}

def test_update_user(client):
	response = client.put('/users/1', json={'name': 'Updated User'})
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'name': 'Updated User', 'recipes': []}

def test_delete_user(client):
	response = client.delete('/users/1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User deleted'}

def test_create_recipe(client):
	response = client.post('/recipes', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'image': 'image_url', 'categories': ['category1', 'category2']})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'image': 'image_url', 'categories': ['category1', 'category2']}

def test_get_recipe(client):
	response = client.get('/recipes/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'image': 'image_url', 'categories': ['category1', 'category2']}

def test_update_recipe(client):
	response = client.put('/recipes/1', json={'name': 'Updated Recipe', 'ingredients': ['updated_ingredient1', 'updated_ingredient2'], 'instructions': ['updated_instruction1', 'updated_instruction2'], 'image': 'updated_image_url', 'categories': ['updated_category1', 'updated_category2']})
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'name': 'Updated Recipe', 'ingredients': ['updated_ingredient1', 'updated_ingredient2'], 'instructions': ['updated_instruction1', 'updated_instruction2'], 'image': 'updated_image_url', 'categories': ['updated_category1', 'updated_category2']}

def test_delete_recipe(client):
	response = client.delete('/recipes/1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe deleted'}
