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


def test_submit_recipe(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/submit_recipe', json={'username': 'test', 'recipe': {'name': 'Test Recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Recipe submitted successfully'}
