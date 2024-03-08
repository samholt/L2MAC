import pytest
from app import app
from models import User, Recipe, Review

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': 1, 'username': 'test', 'password': 'test', 'recipes': [], 'favorites': [], 'follows': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}


def test_create_recipe(client):
	response = client.post('/recipe', json={'id': 1, 'name': 'test', 'ingredients': [], 'instructions': 'test', 'image': 'test', 'categories': [], 'reviews': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}


def test_create_review(client):
	response = client.post('/review', json={'id': 1, 'user_id': 1, 'recipe_id': 1, 'rating': 5, 'comment': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}
