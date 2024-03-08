import pytest
import app
from app import User, Recipe

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}

	response = client.post('/login', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_submit_recipe(client):
	response = client.post('/submit_recipe', json={'username': 'test', 'name': 'test', 'ingredients': ['test'], 'instructions': ['test'], 'images': ['test'], 'categories': ['test']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe submitted successfully'}

	response = client.post('/submit_recipe', json={'username': 'wrong', 'name': 'test', 'ingredients': ['test'], 'instructions': ['test'], 'images': ['test'], 'categories': ['test']})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User does not exist'}

def test_delete_recipe(client):
	response = client.delete('/delete_recipe', json={'username': 'test', 'recipe_name': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe deleted successfully'}

	response = client.delete('/delete_recipe', json={'username': 'test', 'recipe_name': 'wrong'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User or recipe does not exist'}

	response = client.delete('/delete_recipe', json={'username': 'wrong', 'recipe_name': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User or recipe does not exist'}

	response = client.delete('/delete_recipe', json={'username': 'test', 'recipe_name': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User did not submit this recipe'}

def test_edit_recipe(client):
	response = client.put('/edit_recipe', json={'username': 'test', 'recipe_name': 'test', 'new_name': 'new', 'new_ingredients': ['new'], 'new_instructions': ['new'], 'new_images': ['new'], 'new_categories': ['new']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe edited successfully'}

	response = client.put('/edit_recipe', json={'username': 'test', 'recipe_name': 'wrong', 'new_name': 'new', 'new_ingredients': ['new'], 'new_instructions': ['new'], 'new_images': ['new'], 'new_categories': ['new']})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User or recipe does not exist'}

	response = client.put('/edit_recipe', json={'username': 'wrong', 'recipe_name': 'test', 'new_name': 'new', 'new_ingredients': ['new'], 'new_instructions': ['new'], 'new_images': ['new'], 'new_categories': ['new']})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User or recipe does not exist'}

	response = client.put('/edit_recipe', json={'username': 'test', 'recipe_name': 'test', 'new_name': 'new', 'new_ingredients': ['new'], 'new_instructions': ['new'], 'new_images': ['new'], 'new_categories': ['new']})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User did not submit this recipe'}
