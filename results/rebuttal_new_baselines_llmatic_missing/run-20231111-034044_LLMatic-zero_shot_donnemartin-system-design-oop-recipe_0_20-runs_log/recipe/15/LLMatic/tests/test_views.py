import json
import pytest
from views import app, user_service, recipe_service
from models import User, Recipe, Review, Follow

@pytest.fixture(autouse=True)
def setup():
	# Create a user and a recipe for testing
	user = user_service.create_user('test', 'password', 'test@test.com', [])
	recipe = recipe_service.create_recipe('test recipe', 'test ingredients', 'test instructions', 'test image', ['test category'], 'test')
	user_service.save_favorite_recipe('test', 'test recipe')
	print(f'User created: {user.username}')
	print(f'Recipe created: {recipe.name}')

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_submit_recipe(client):
	response = client.post('/submit_recipe', json={'name': 'test recipe', 'ingredients': 'test ingredients', 'instructions': 'test instructions', 'image': 'test image', 'categories': ['test category'], 'submitted_by': 'test'})
	print(f'Status code: {response.status_code}')
	assert response.status_code == 200


def test_manage_recipe(client):
	response = client.post('/manage_recipe', json={'name': 'test recipe', 'ingredients': 'test ingredients', 'instructions': 'test instructions', 'image': 'test image', 'categories': ['test category'], 'submitted_by': 'test'})
	print(f'Status code: {response.status_code}')
	assert response.status_code == 200


def test_search(client):
	response = client.get('/search?name=test recipe')
	print(f'Status code: {response.status_code}')
	assert response.status_code == 200


def test_save_favorite(client):
	response = client.post('/save_favorite', json={'username': 'test', 'recipe_name': 'test recipe'})
	print(f'Status code: {response.status_code}')
	assert response.status_code == 200


def test_profile(client):
	response = client.get('/profile?username=test')
	print(f'Status code: {response.status_code}')
	assert response.status_code == 200


def test_recommendations(client):
	response = client.get('/recommendations?username=test')
	print(f'Status code: {response.status_code}')
	assert response.status_code == 200

# Admin routes tests
def test_manage_recipes(client):
	# Test GET method
	response = client.get('/admin/manage_recipes')
	print(f'Status code: {response.status_code}')
	assert response.status_code == 200

	# Test POST method
	response = client.post('/admin/manage_recipes', json={'name': 'test recipe', 'ingredients': 'test ingredients', 'instructions': 'test instructions', 'image': 'test image', 'categories': ['test category'], 'submitted_by': 'test'})
	print(f'Status code: {response.status_code}')
	assert response.status_code == 200

	# Test DELETE method
	response = client.delete('/admin/manage_recipes', json={'name': 'test recipe'})
	print(f'Status code: {response.status_code}')
	assert response.status_code == 200


def test_site_statistics(client):
	response = client.get('/admin/site_statistics')
	print(f'Status code: {response.status_code}')
	assert response.status_code == 200

