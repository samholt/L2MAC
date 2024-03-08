import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={
		'name': 'Test User',
		'email': 'test@example.com',
		'password': 'password',
		'recipes': [],
		'favorites': []
	})
	assert response.status_code == 201
	assert response.get_json()['name'] == 'Test User'


def test_create_recipe(client):
	response = client.post('/recipe', json={
		'name': 'Test Recipe',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2']
	})
	assert response.status_code == 201
	assert response.get_json()['name'] == 'Test Recipe'
