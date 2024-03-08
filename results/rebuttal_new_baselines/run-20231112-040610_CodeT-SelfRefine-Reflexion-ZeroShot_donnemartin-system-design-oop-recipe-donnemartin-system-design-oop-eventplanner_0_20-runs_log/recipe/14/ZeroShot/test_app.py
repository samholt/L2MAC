import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': '1', 'name': 'Test User', 'recipes': [], 'favorites': [], 'followers': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Test User', 'recipes': [], 'favorites': [], 'followers': []}


def test_create_recipe(client):
	response = client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': [], 'instructions': [], 'images': [], 'categories': [], 'reviews': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Test Recipe', 'ingredients': [], 'instructions': [], 'images': [], 'categories': [], 'reviews': []}
