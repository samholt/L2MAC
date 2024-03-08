import pytest
import app
from app import User, Recipe

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/user', json={'id': '1', 'name': 'Test User', 'recipes': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}

def test_get_user(client):
	app.users['1'] = User(id='1', name='Test User', recipes=[])
	response = client.get('/user/1')
	assert response.status_code == 200
	assert response.get_json() == {'user': {'id': '1', 'name': 'Test User', 'recipes': []}}

def test_update_user(client):
	app.users['1'] = User(id='1', name='Test User', recipes=[])
	response = client.put('/user/1', json={'name': 'Updated User', 'recipes': ['1']})
	assert response.status_code == 200
	assert response.get_json() == {'user': {'id': '1', 'name': 'Updated User', 'recipes': ['1']}}

def test_delete_user(client):
	app.users['1'] = User(id='1', name='Test User', recipes=[])
	response = client.delete('/user/1')
	assert response.status_code == 204

def test_create_recipe(client):
	response = client.post('/recipe', json={'id': '1', 'name': 'Test Recipe', 'ingredients': ['Ingredient 1'], 'instructions': ['Instruction 1'], 'image': 'image.jpg', 'categories': ['Category 1']})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1'}

def test_get_recipe(client):
	app.recipes['1'] = Recipe(id='1', name='Test Recipe', 'ingredients': ['Ingredient 1'], 'instructions': ['Instruction 1'], 'image': 'image.jpg', 'categories': ['Category 1'])
	response = client.get('/recipe/1')
	assert response.status_code == 200
	assert response.get_json() == {'recipe': {'id': '1', 'name': 'Test Recipe', 'ingredients': ['Ingredient 1'], 'instructions': ['Instruction 1'], 'image': 'image.jpg', 'categories': ['Category 1']}}

def test_update_recipe(client):
	app.recipes['1'] = Recipe(id='1', name='Test Recipe', 'ingredients': ['Ingredient 1'], 'instructions': ['Instruction 1'], 'image': 'image.jpg', 'categories': ['Category 1'])
	response = client.put('/recipe/1', json={'name': 'Updated Recipe', 'ingredients': ['Updated Ingredient'], 'instructions': ['Updated Instruction'], 'image': 'updated_image.jpg', 'categories': ['Updated Category']})
	assert response.status_code == 200
	assert response.get_json() == {'recipe': {'id': '1', 'name': 'Updated Recipe', 'ingredients': ['Updated Ingredient'], 'instructions': ['Updated Instruction'], 'image': 'updated_image.jpg', 'categories': ['Updated Category']}}

def test_delete_recipe(client):
	app.recipes['1'] = Recipe(id='1', name='Test Recipe', 'ingredients': ['Ingredient 1'], 'instructions': ['Instruction 1'], 'image': 'image.jpg', 'categories': ['Category 1'])
	response = client.delete('/recipe/1')
	assert response.status_code == 204
