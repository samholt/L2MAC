import pytest
import app
from app import User, Recipe, Review

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	user = User(id='1', name='Test User', recipes=[], favorites=[])
	response = client.post('/users', json=user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == user.__dict__


def test_create_recipe(client):
	recipe = Recipe(id='1', name='Test Recipe', ingredients=[], instructions=[], images=[], categories=[])
	response = client.post('/recipes', json=recipe.__dict__)
	assert response.status_code == 201
	assert response.get_json() == recipe.__dict__


def test_create_review(client):
	review = Review(id='1', user_id='1', recipe_id='1', rating=5, comment='Great recipe!')
	response = client.post('/reviews', json=review.__dict__)
	assert response.status_code == 201
	assert response.get_json() == review.__dict__
