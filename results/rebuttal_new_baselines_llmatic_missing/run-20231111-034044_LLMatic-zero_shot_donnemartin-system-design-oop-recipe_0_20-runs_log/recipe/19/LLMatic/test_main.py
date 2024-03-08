import pytest
import main
from flask import Flask, request

@pytest.fixture
def client():
	main.app.config['TESTING'] = True
	with main.app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.data == b'Hello, World!'


def test_create_account(client):
	response = client.post('/create_account', json={'username': 'test', 'password': 'test'})
	assert response.data == b'Account created successfully'


def test_submit_recipe(client):
	response = client.post('/submit_recipe', json={'name': 'test', 'ingredients': ['test'], 'instructions': 'test', 'images': ['test'], 'categories': ['test']})
	assert response.data == b'Recipe submitted successfully'


def test_search(client):
	response = client.get('/search', json={'name': 'test'})
	assert 'results' in response.get_json()

