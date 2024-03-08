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
	assert app.User.query.filter_by(username='test').first() is not None

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200

def test_submit_recipe(client):
	response = client.post('/submit_recipe', json={'username': 'test', 'name': 'test recipe', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': ['instruction1', 'instruction2'], 'images': ['image1', 'image2'], 'categories': ['category1', 'category2']})
	assert response.status_code == 200
	assert app.Recipe.query.get(1) is not None

def test_edit_recipe(client):
	response = client.post('/edit_recipe', json={'username': 'test', 'recipe_id': 1, 'name': 'edited recipe'})
	assert response.status_code == 200
	assert app.Recipe.query.get(1).name == 'edited recipe'

def test_delete_recipe(client):
	response = client.post('/delete_recipe', json={'username': 'test', 'recipe_id': 1})
	assert response.status_code == 200
	assert app.Recipe.query.get(1) is None
