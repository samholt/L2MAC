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


def test_create_recipe(client):
	response = client.post('/recipe', json={
		'id': '1',
		'name': 'Test Recipe',
		'ingredients': ['Ingredient 1', 'Ingredient 2'],
		'instructions': ['Instruction 1', 'Instruction 2'],
		'images': ['Image 1', 'Image 2'],
		'categories': ['Category 1', 'Category 2'],
		'reviews': []
	})
	assert response.status_code == 201
	assert response.get_json() == {
		'id': '1',
		'name': 'Test Recipe',
		'ingredients': ['Ingredient 1', 'Ingredient 2'],
		'instructions': ['Instruction 1', 'Instruction 2'],
		'images': ['Image 1', 'Image 2'],
		'categories': ['Category 1', 'Category 2'],
		'reviews': []
	}
