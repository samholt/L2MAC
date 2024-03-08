import pytest
import app
from app import User, Recipe

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'name': 'John', 'email': 'john@example.com', 'password': 'password', 'recipes': []})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'John', 'email': 'john@example.com', 'password': 'password', 'recipes': []}


def test_create_recipe(client):
	response = client.post('/recipe', json={'name': 'Pizza', 'ingredients': ['Flour', 'Water', 'Yeast'], 'instructions': ['Mix ingredients', 'Bake'], 'image': 'pizza.jpg', 'category': 'Italian'})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'Pizza', 'ingredients': ['Flour', 'Water', 'Yeast'], 'instructions': ['Mix ingredients', 'Bake'], 'image': 'pizza.jpg', 'category': 'Italian'}


def test_get_recipe(client):
	app.recipes['Pizza'] = Recipe('Pizza', ['Flour', 'Water', 'Yeast'], ['Mix ingredients', 'Bake'], 'pizza.jpg', 'Italian')
	response = client.get('/recipe/Pizza')
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Pizza', 'ingredients': ['Flour', 'Water', 'Yeast'], 'instructions': ['Mix ingredients', 'Bake'], 'image': 'pizza.jpg', 'category': 'Italian'}


def test_update_recipe(client):
	app.recipes['Pizza'] = Recipe('Pizza', ['Flour', 'Water', 'Yeast'], ['Mix ingredients', 'Bake'], 'pizza.jpg', 'Italian')
	response = client.put('/recipe/Pizza', json={'name': 'Pizza', 'ingredients': ['Flour', 'Water', 'Yeast', 'Tomato Sauce'], 'instructions': ['Mix ingredients', 'Bake'], 'image': 'pizza.jpg', 'category': 'Italian'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Pizza', 'ingredients': ['Flour', 'Water', 'Yeast', 'Tomato Sauce'], 'instructions': ['Mix ingredients', 'Bake'], 'image': 'pizza.jpg', 'category': 'Italian'}


def test_delete_recipe(client):
	app.recipes['Pizza'] = Recipe('Pizza', ['Flour', 'Water', 'Yeast'], ['Mix ingredients', 'Bake'], 'pizza.jpg', 'Italian')
	response = client.delete('/recipe/Pizza')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe deleted'}
