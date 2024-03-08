import pytest
import app
from models import User, Recipe, Review

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': 1, 'username': 'test', 'email': 'test@test.com', 'favorites': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}


def test_create_recipe(client):
	response = client.post('/recipe', json={'id': 1, 'name': 'test', 'ingredients': ['test'], 'instructions': 'test', 'image': 'test', 'category': 'test', 'reviews': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}


def test_add_favorite(client):
	client.post('/user', json={'id': 1, 'username': 'test', 'email': 'test@test.com', 'favorites': []})
	client.post('/recipe', json={'id': 1, 'name': 'test', 'ingredients': ['test'], 'instructions': 'test', 'image': 'test', 'category': 'test', 'reviews': []})
	response = client.post('/user/1/favorite', json={'recipe_id': 1})
	assert response.status_code == 204


def test_create_review(client):
	client.post('/user', json={'id': 1, 'username': 'test', 'email': 'test@test.com', 'favorites': []})
	client.post('/recipe', json={'id': 1, 'name': 'test', 'ingredients': ['test'], 'instructions': 'test', 'image': 'test', 'category': 'test', 'reviews': []})
	response = client.post('/review', json={'id': 1, 'user_id': 1, 'recipe_id': 1, 'rating': 5, 'comment': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}
