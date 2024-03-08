import pytest
from app import app, users, recipes, reviews

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': 1, 'username': 'test', 'email': 'test@test.com', 'favorite_recipes': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}
	assert users[1].username == 'test'


def test_create_recipe(client):
	response = client.post('/recipe', json={'id': 1, 'name': 'test', 'ingredients': ['test'], 'instructions': 'test', 'image': 'test', 'category': 'test', 'reviews': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}
	assert recipes[1].name == 'test'


def test_create_review(client):
	response = client.post('/review', json={'id': 1, 'user_id': 1, 'recipe_id': 1, 'rating': 5, 'comment': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}
	assert reviews[1].rating == 5


def test_add_favorite(client):
	client.post('/user', json={'id': 1, 'username': 'test', 'email': 'test@test.com', 'favorite_recipes': []})
	client.post('/recipe', json={'id': 1, 'name': 'test', 'ingredients': ['test'], 'instructions': 'test', 'image': 'test', 'category': 'test', 'reviews': []})
	response = client.post('/user/1/favorite', json={'recipe_id': 1})
	assert response.status_code == 204
	assert 1 in users[1].favorite_recipes
