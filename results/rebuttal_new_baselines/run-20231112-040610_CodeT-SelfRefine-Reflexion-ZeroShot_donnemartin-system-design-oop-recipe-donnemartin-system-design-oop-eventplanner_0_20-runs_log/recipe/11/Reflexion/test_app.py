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
	response = client.post('/users', json=app.dataclass_to_dict(user))
	assert response.status_code == 201
	assert response.get_json() == app.dataclass_to_dict(user)


def test_create_recipe(client):
	recipe = Recipe(id='1', name='Test Recipe', ingredients=['ingredient1', 'ingredient2'], instructions='Test instructions', image='Test image', user_id='1')
	response = client.post('/recipes', json=app.dataclass_to_dict(recipe))
	assert response.status_code == 201
	assert response.get_json() == app.dataclass_to_dict(recipe)
