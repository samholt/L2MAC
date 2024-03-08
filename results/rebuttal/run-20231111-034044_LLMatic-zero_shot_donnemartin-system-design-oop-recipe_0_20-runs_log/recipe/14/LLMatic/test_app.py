import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': '1', 'name': 'Test User', 'email': 'test@example.com'})
	assert response.get_json() == 'User created successfully'


def test_get_user(client):
	response = client.get('/user/1')
	assert response.get_json() == {'id': '1', 'name': 'Test User', 'email': 'test@example.com', 'following': [], 'feed': [], 'liked_recipes': []}


def test_update_user(client):
	response = client.put('/user/1', json={'name': 'Updated User', 'email': 'updated@example.com'})
	assert response.get_json() == 'User updated successfully'


def test_delete_user(client):
	response = client.delete('/user/1')
	assert response.get_json() == 'User deleted successfully'


def test_submit_recipe(client):
	response = client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': 'Test instructions', 'category': 'Test category'})
	assert response.get_json() == {'status': 'Recipe submitted successfully'}


def test_get_recipe(client):
	response = client.get('/recipe/1')
	assert response.get_json() == {'id': '1', 'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': 'Test instructions', 'category': 'Test category'}


def test_edit_recipe(client):
	response = client.put('/recipe/1', json={'name': 'Updated Recipe', 'ingredients': ['ingredient1', 'ingredient2', 'ingredient3'], 'instructions': 'Updated instructions', 'category': 'Updated category'})
	assert response.get_json() == {'status': 'Recipe updated successfully'}


def test_delete_recipe(client):
	response = client.delete('/recipe/1')
	assert response.get_json() == {'status': 'Recipe deleted successfully'}


def test_add_review(client):
	response = client.post('/review', json={'user_id': '1', 'recipe_id': '1', 'rating': 5, 'review': 'Test review'})
	assert response.get_json() == {'status': 'success', 'message': 'Review added successfully'}


def test_get_reviews(client):
	response = client.get('/review/1')
	assert response.get_json() == {'status': 'success', 'data': [{'user_id': '1', 'rating': 5, 'review': 'Test review'}]}


def test_add_category(client):
	response = client.post('/category', json={'category_type': 'type', 'category': 'Test category'})
	assert response.get_json() == {'status': 'Category added successfully'}


def test_get_categories(client):
	response = client.get('/category/type')
	assert response.get_json() == ['Test category']


def test_get_recommendations(client):
	response = client.get('/recommendation/1')
	assert isinstance(response.get_json(), dict)
	assert response.get_json() == {'error': 'User not found'}
	response = client.get('/recommendation/2')
	assert response.get_json() == {'error': 'User not found'}
