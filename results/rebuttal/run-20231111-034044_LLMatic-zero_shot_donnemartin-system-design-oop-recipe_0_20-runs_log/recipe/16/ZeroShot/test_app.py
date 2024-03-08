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

def test_get_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': [], 'instructions': [], 'images': [], 'categories': [], 'reviews': []})
	response = client.get('/recipe/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'name': 'Test Recipe', 'ingredients': [], 'instructions': [], 'images': [], 'categories': [], 'reviews': []}

def test_delete_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': [], 'instructions': [], 'images': [], 'categories': [], 'reviews': []})
	response = client.delete('/recipe/1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe deleted'}

def test_update_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': [], 'instructions': [], 'images': [], 'categories': [], 'reviews': []})
	response = client.put('/recipe/1', json={'name': 'Updated Recipe'})
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'name': 'Updated Recipe', 'ingredients': [], 'instructions': [], 'images': [], 'categories': [], 'reviews': []}
