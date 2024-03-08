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
	assert response.get_json()['id'] == '1'
	assert response.get_json()['name'] == 'Test User'


def test_create_recipe(client):
	response = client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	assert response.status_code == 201
	assert response.get_json()['id'] == '1'
	assert response.get_json()['name'] == 'Test Recipe'


def test_update_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	response = client.put('/recipe/1', json={'name': 'Updated Recipe'})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'Updated Recipe'


def test_delete_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	response = client.delete('/recipe/1')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Recipe deleted'
