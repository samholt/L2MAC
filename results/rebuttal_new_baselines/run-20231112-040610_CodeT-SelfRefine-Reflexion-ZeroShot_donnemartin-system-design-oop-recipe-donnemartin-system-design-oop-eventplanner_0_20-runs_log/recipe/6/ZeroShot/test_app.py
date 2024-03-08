import pytest
import app
from app import User, Recipe

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def new_user():
	user = User('Test User', 'test@example.com', [], [])
	return user

@pytest.fixture
def new_recipe():
	recipe = Recipe('Test Recipe', ['ingredient1', 'ingredient2'], ['instruction1', 'instruction2'], ['image1', 'image2'], ['category1', 'category2'])
	return recipe


def test_create_user(client, new_user):
	response = client.post('/user', json=new_user.__dict__)
	assert response.status_code == 201
	assert response.get_json()['name'] == new_user.name


def test_create_recipe(client, new_recipe):
	response = client.post('/recipe', json=new_recipe.__dict__)
	assert response.status_code == 201
	assert response.get_json()['name'] == new_recipe.name


def test_get_recipes(client, new_recipe):
	client.post('/recipe', json=new_recipe.__dict__)
	response = client.get('/recipe')
	assert response.status_code == 200
	assert new_recipe.name in response.get_json()


def test_get_recipe(client, new_recipe):
	client.post('/recipe', json=new_recipe.__dict__)
	response = client.get(f'/recipe/{new_recipe.name}')
	assert response.status_code == 200
	assert response.get_json()['name'] == new_recipe.name
