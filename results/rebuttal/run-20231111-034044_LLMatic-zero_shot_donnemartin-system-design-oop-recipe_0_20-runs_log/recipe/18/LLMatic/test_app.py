import pytest
from flask import url_for
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Welcome to Home Page'


def test_user_page(client):
	response = client.get('/user')
	assert response.status_code == 200
	assert response.data == b'User Page'


def test_recipe_page(client):
	response = client.get('/recipe')
	assert response.status_code == 200
	assert response.data == b'Recipe Page'


def test_search_page(client):
	response = client.get('/search')
	assert response.status_code == 200
	assert response.data == b'Search Page'


def test_rating_page(client):
	response = client.get('/rating')
	assert response.status_code == 200
	assert response.data == b'Rating Page'


def test_admin_page(client):
	response = client.get('/admin')
	assert response.status_code == 200
	assert response.data == b'Admin Page'
