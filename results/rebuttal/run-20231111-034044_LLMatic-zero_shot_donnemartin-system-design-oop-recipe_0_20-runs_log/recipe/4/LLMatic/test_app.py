import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_get_recipes(client):
	response = client.get('/recipes', json={'id': 1})
	assert response.status_code == 200


def test_post_recipes(client):
	response = client.post('/recipes', json={'id': 1, 'recipe': {'name': 'test', 'ingredients': ['test'], 'steps': ['test']}})
	assert response.status_code == 200


def test_get_users(client):
	response = client.get('/users', json={'id': 1})
	assert response.status_code == 200


def test_post_users(client):
	response = client.post('/users', json={'id': 1, 'name': 'test', 'email': 'test@test.com'})
	assert response.status_code == 200


def test_get_reviews(client):
	response = client.get('/reviews', json={'recipe_id': 1})
	assert response.status_code == 200


def test_post_reviews(client):
	response = client.post('/reviews', json={'user_id': 1, 'recipe_id': 1, 'rating': 5, 'review': 'test'})
	assert response.status_code == 200


def test_get_categories(client):
	response = client.get('/categories', json={'type': 'test'})
	assert response.status_code == 200


def test_post_categories(client):
	response = client.post('/categories', json={'type': 'test', 'name': 'test'})
	assert response.status_code == 200


def test_get_admins(client):
	response = client.get('/admin', json={'user_id': 1})
	assert response.status_code == 200


def test_post_admins(client):
	response = client.post('/admin', json={'recipe_id': 1, 'action': 'delete'})
	assert response.status_code == 200


def test_get_recommendations(client):
	response = client.get('/recommendations', json={'user_id': 1})
	assert response.status_code == 200
