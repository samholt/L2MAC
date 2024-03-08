import pytest
import app
from app import User, Recipe

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_submit_recipe(client):
	recipe = Recipe(id='1', name='Test Recipe', ingredients=['ingredient1', 'ingredient2'], instructions=['step1', 'step2'], images=['image1', 'image2'], categories=['category1', 'category2'], reviews=[])
	response = client.post('/submit_recipe', json=recipe.__dict__)
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe submitted successfully'}

def test_edit_recipe(client):
	recipe = {'name': 'Updated Recipe'}
	response = client.put('/edit_recipe/1', json=recipe)
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe updated successfully'}

def test_delete_recipe(client):
	response = client.delete('/delete_recipe/1')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe deleted successfully'}

def test_search_recipes(client):
	response = client.get('/search_recipes?query=category1')
	assert response.status_code == 200

def test_create_user(client):
	user = User(id='1', name='Test User', recipes=[], favorites=[])
	response = client.post('/create_user', json=user.__dict__)
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User created successfully'}

def test_rate_recipe(client):
	rating = {'user_id': '1', 'rating': 5, 'review': 'Great recipe!'}
	response = client.post('/rate_recipe/1', json=rating)
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Rating submitted successfully'}
