import pytest
import app

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


def test_submit_recipe(client):
	response = client.post('/submit_recipe', json={'username': 'test', 'recipe_name': 'test_recipe', 'ingredients': 'test_ingredients', 'instructions': 'test_instructions', 'image': 'test_image', 'category': 'test_category'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User does not exist'}

	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/submit_recipe', json={'username': 'test', 'recipe_name': 'test_recipe', 'ingredients': 'test_ingredients', 'instructions': 'test_instructions', 'image': 'test_image', 'category': 'test_category'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe submitted successfully'}
