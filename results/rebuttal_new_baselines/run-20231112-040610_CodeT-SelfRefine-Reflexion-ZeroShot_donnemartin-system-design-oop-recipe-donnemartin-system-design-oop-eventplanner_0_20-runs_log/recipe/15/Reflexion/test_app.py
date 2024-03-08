import pytest
import app
from app import User, Recipe, Review

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return User(id='1', name='Test User', favorites=[])

@pytest.fixture
def recipe():
	return Recipe(id='1', name='Test Recipe', ingredients=[], instructions=[], images=[], categories=[])

@pytest.fixture
def review():
	return Review(id='1', user_id='1', recipe_id='1', rating=5, comment='Great recipe!')


def test_create_user(client, user):
	response = client.post('/user', json=user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == user.__dict__


def test_create_recipe(client, recipe):
	response = client.post('/recipe', json=recipe.__dict__)
	assert response.status_code == 201
	assert response.get_json() == recipe.__dict__


def test_create_review(client, review):
	response = client.post('/review', json=review.__dict__)
	assert response.status_code == 201
	assert response.get_json() == review.__dict__
