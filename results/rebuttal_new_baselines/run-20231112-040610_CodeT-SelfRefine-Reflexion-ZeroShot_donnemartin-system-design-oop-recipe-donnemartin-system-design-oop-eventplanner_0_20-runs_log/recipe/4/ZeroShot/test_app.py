import pytest
import app
from app import User, Recipe

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
	response = client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['Test Ingredient'], 'instructions': ['Test Instruction'], 'images': ['Test Image'], 'categories': ['Test Category'], 'reviews': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Test Recipe', 'ingredients': ['Test Ingredient'], 'instructions': ['Test Instruction'], 'images': ['Test Image'], 'categories': ['Test Category'], 'reviews': []}

def test_update_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['Test Ingredient'], 'instructions': ['Test Instruction'], 'images': ['Test Image'], 'categories': ['Test Category'], 'reviews': []})
	response = client.put('/recipe/1', json={'name': 'Updated Recipe'})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'Updated Recipe'

def test_delete_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['Test Ingredient'], 'instructions': ['Test Instruction'], 'images': ['Test Image'], 'categories': ['Test Category'], 'reviews': []})
	response = client.delete('/recipe/1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe deleted'}

def test_search_recipe(client):
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['Test Ingredient'], 'instructions': ['Test Instruction'], 'images': ['Test Image'], 'categories': ['Test Category'], 'reviews': []})
	response = client.get('/recipe/search?query=Test')
	assert response.status_code == 200
	assert len(response.get_json()) == 1

def test_add_favorite(client):
	client.post('/user', json={'id': '1', 'name': 'Test User', 'recipes': [], 'favorites': []})
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['Test Ingredient'], 'instructions': ['Test Instruction'], 'images': ['Test Image'], 'categories': ['Test Category'], 'reviews': []})
	response = client.post('/user/1/favorites', json={'recipe_id': '1'})
	assert response.status_code == 200
	assert len(response.get_json()['favorites']) == 1

def test_get_user_recipes(client):
	client.post('/user', json={'id': '1', 'name': 'Test User', 'recipes': [], 'favorites': []})
	response = client.get('/user/1/recipes')
	assert response.status_code == 200
	assert len(response.get_json()) == 0

def test_get_user_favorites(client):
	client.post('/user', json={'id': '1', 'name': 'Test User', 'recipes': [], 'favorites': []})
	client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['Test Ingredient'], 'instructions': ['Test Instruction'], 'images': ['Test Image'], 'categories': ['Test Category'], 'reviews': []})
	client.post('/user/1/favorites', json={'recipe_id': '1'})
	response = client.get('/user/1/favorites')
	assert response.status_code == 200
	assert len(response.get_json()) == 1
