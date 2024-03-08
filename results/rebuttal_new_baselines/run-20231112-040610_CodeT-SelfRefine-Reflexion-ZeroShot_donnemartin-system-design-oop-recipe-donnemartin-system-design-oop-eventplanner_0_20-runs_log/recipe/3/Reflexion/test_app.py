import pytest
import app
from app import User, Recipe, Review

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'id': '1', 'username': 'test', 'password': 'test', 'recipes': [], 'favorites': [], 'following': []})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'username': 'test', 'password': 'test', 'recipes': [], 'favorites': [], 'following': []}

def test_login(client):
	response = client.post('/login', json={'id': '1', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'username': 'test', 'password': 'test', 'recipes': [], 'favorites': [], 'following': []}

def test_submit_recipe(client):
	response = client.post('/submit_recipe', json={'id': '1', 'name': 'test', 'ingredients': ['test'], 'instructions': ['test'], 'images': ['test'], 'category': 'test', 'user_id': '1'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'test', 'ingredients': ['test'], 'instructions': ['test'], 'images': ['test'], 'category': 'test', 'user_id': '1'}

def test_search_recipe(client):
	response = client.get('/search_recipe', query_string={'name': 'test'})
	assert response.status_code == 200
	assert response.get_json() == [{'id': '1', 'name': 'test', 'ingredients': ['test'], 'instructions': ['test'], 'images': ['test'], 'category': 'test', 'user_id': '1'}]
