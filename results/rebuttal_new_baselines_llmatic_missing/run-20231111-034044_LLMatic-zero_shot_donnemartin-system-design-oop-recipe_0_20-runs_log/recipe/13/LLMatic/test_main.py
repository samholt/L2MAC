import pytest
import main
from flask import json

@pytest.fixture
def client():
	main.app.config['TESTING'] = True
	with main.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully.'}


def test_create_recipe(client):
	response = client.post('/recipe', json={'name': 'test', 'ingredients': ['test'], 'instructions': 'test', 'images': ['test'], 'categories': ['test']})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Recipe created successfully.'}


def test_search(client):
	response = client.get('/search?name=test')
	assert response.status_code == 200
	assert json.loads(response.data) == {'result': ['test']}
