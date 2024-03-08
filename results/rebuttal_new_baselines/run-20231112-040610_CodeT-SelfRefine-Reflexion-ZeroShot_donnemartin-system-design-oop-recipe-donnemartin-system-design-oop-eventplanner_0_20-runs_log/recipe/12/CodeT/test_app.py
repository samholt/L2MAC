import pytest
import app
from app import User, Recipe

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	user = User(id='1', name='Test User', recipes=[], favorites=[])
	response = client.post('/user', json=user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == user.__dict__


def test_create_recipe(client):
	recipe = Recipe(id='1', name='Test Recipe', ingredients=[], instructions=[], images=[], categories=[], reviews=[])
	response = client.post('/recipe', json=recipe.__dict__)
	assert response.status_code == 201
	assert response.get_json() == recipe.__dict__
