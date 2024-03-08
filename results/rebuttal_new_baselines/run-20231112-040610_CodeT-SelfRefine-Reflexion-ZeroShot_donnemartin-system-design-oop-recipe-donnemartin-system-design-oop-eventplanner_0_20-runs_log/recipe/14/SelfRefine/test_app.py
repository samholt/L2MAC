import pytest
import app

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
	assert response.get_json() == {
		'id': '1',
		'name': 'Test User',
		'recipes': [],
		'favorites': []
	}


def test_get_user(client):
	response = client.get('/user/1')
	assert response.status_code == 200
	assert response.get_json() == {
		'id': '1',
		'name': 'Test User',
		'recipes': [],
		'favorites': []
	}


def test_update_user(client):
	response = client.put('/user/1', json={
		'id': '1',
		'name': 'Updated User',
		'recipes': [],
		'favorites': []
	})
	assert response.status_code == 200
	assert response.get_json() == {
		'id': '1',
		'name': 'Updated User',
		'recipes': [],
		'favorites': []
	}


def test_delete_user(client):
	response = client.delete('/user/1')
	assert response.status_code == 204


def test_create_recipe(client):
	response = client.post('/recipe', json={
		'id': '1',
		'name': 'Test Recipe',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2']
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'Test Recipe',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2']
	}


def test_get_recipe(client):
	response = client.get('/recipe/1')
	assert response.status_code == 200
	assert response.get_json() == {
		'id': '1',
		'name': 'Test Recipe',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2']
	}


def test_update_recipe(client):
	response = client.put('/recipe/1', json={
		'id': '1',
		'name': 'Updated Recipe',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2']
	})
	assert response.status_code == 200
	assert response.get_json() == {
		'id': '1',
		'name': 'Updated Recipe',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2']
	}


def test_delete_recipe(client):
	response = client.delete('/recipe/1')
	assert response.status_code == 204


def test_create_review(client):
	response = client.post('/review', json={
		'id': '1',
		'user_id': '1',
		'recipe_id': '1',
		'rating': 5,
		'comment': 'Great recipe!'
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'user_id': '1',
		'recipe_id': '1',
		'rating': 5,
		'comment': 'Great recipe!'
	}


def test_get_review(client):
	response = client.get('/review/1')
	assert response.status_code == 200
	assert response.get_json() == {
		'id': '1',
		'user_id': '1',
		'recipe_id': '1',
		'rating': 5,
		'comment': 'Great recipe!'
	}


def test_update_review(client):
	response = client.put('/review/1', json={
		'id': '1',
		'user_id': '1',
		'recipe_id': '1',
		'rating': 4,
		'comment': 'Good recipe!'
	})
	assert response.status_code == 200
	assert response.get_json() == {
		'id': '1',
		'user_id': '1',
		'recipe_id': '1',
		'rating': 4,
		'comment': 'Good recipe!'
	}


def test_delete_review(client):
	response = client.delete('/review/1')
	assert response.status_code == 204
