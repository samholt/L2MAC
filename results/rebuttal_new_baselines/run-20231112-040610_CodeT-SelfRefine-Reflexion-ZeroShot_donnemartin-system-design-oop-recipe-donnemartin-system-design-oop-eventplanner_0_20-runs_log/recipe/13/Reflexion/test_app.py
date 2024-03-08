import pytest
import app
from app import User, Recipe

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	user = User(id='1', name='Test User')
	response = client.post('/users', json=user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == user.__dict__


def test_create_recipe(client):
	recipe = Recipe(id='1', name='Test Recipe', ingredients=['ingredient1', 'ingredient2'], instructions=['step1', 'step2'], image='image_url', user_id='1')
	response = client.post('/recipes', json=recipe.__dict__)
	assert response.status_code == 201
	assert response.get_json() == recipe.__dict__
