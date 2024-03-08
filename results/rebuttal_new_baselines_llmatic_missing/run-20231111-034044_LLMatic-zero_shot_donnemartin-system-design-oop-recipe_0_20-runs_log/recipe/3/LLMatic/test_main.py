import pytest
import main


def test_create_account():
	response = main.app.test_client().post('/create_account', json={'username': 'test', 'password': 'test', 'preferences': ['test']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Account created successfully', 'user': {'username': 'test', 'preferences': ['test']}}


def test_submit_recipe():
	response = main.app.test_client().post('/submit_recipe', json={'name': 'test', 'category': 'test', 'instructions': 'test', 'submitted_by': 'test'})
	assert response.status_code == 200


def test_search_recipe():
	response = main.app.test_client().get('/search_recipe', json={'name': 'test', 'category': 'test', 'instructions': 'test', 'submitted_by': 'test'})
	assert response.status_code == 200
