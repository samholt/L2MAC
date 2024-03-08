import pytest
from app import app
from models import User, Recipe


def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'New user created'}

def test_create_recipe(client):
	response = client.post('/recipe', json={'title': 'test recipe', 'instructions': 'test instructions', 'user_id': 1})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'New recipe created'}
