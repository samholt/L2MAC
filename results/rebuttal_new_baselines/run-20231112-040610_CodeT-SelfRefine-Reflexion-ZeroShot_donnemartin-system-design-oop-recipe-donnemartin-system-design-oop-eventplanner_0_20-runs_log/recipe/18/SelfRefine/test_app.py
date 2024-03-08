import pytest
import app
from app import db, User, Recipe

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={
		'id': '1',
		'name': 'Test User',
		'recipes': [],
		'favorites': []
	})
	assert response.status_code == 201
	user = User.query.get('1')
	assert user is not None

	# Test creating a user with an existing id
	response = client.post('/user', json={
		'id': '1',
		'name': 'Test User 2',
		'recipes': [],
		'favorites': []
	})
	assert response.status_code == 400

	# Test creating a user with missing fields
	response = client.post('/user', json={
		'id': '2',
		'recipes': [],
		'favorites': []
	})
	assert response.status_code == 400


def test_create_recipe(client):
	response = client.post('/recipe', json={
		'id': '1',
		'name': 'Test Recipe',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2'],
		'reviews': []
	})
	assert response.status_code == 201
	recipe = Recipe.query.get('1')
	assert recipe is not None

	# Test creating a recipe with an existing id
	response = client.post('/recipe', json={
		'id': '1',
		'name': 'Test Recipe 2',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2'],
		'reviews': []
	})
	assert response.status_code == 400

	# Test creating a recipe with missing fields
	response = client.post('/recipe', json={
		'id': '2',
		'name': 'Test Recipe 2',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'reviews': []
	})
	assert response.status_code == 400
