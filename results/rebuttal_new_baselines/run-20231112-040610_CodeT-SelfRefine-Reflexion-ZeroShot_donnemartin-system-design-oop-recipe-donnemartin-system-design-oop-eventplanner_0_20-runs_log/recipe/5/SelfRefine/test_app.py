import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'name': 'John Doe', 'email': 'john@example.com', 'recipes': [], 'favorites': []})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'John Doe', 'email': 'john@example.com', 'recipes': [], 'favorites': []}


def test_create_recipe(client):
	response = client.post('/recipe', json={'name': 'Pancakes', 'ingredients': ['flour', 'milk', 'eggs'], 'instructions': ['Mix ingredients', 'Cook on pan'], 'images': [], 'categories': ['breakfast']})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'Pancakes', 'ingredients': ['flour', 'milk', 'eggs'], 'instructions': ['Mix ingredients', 'Cook on pan'], 'images': [], 'categories': ['breakfast']}


def test_get_recipes(client):
	response = client.get('/recipe')
	assert response.status_code == 200


def test_get_recipe(client):
	response = client.get('/recipe/Pancakes')
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Pancakes', 'ingredients': ['flour', 'milk', 'eggs'], 'instructions': ['Mix ingredients', 'Cook on pan'], 'images': [], 'categories': ['breakfast']}
