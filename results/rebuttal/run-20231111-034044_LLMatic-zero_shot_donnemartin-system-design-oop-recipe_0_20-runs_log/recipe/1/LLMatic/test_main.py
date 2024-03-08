import pytest
import main
from flask import json


def test_create_account():
	response = main.app.test_client().post('/create_account',
		data=json.dumps(dict(username='test', password='test')),
		content_type='application/json',
	)
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 201
	assert data['message'] == 'Account created successfully'


def test_submit_recipe():
	response = main.app.test_client().post('/submit_recipe',
		data=json.dumps(dict(ingredients='test', instructions='test', images='test', category='test', dietary_needs='test', timestamp='test')),
		content_type='application/json',
	)
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 201
	assert data['message'] == 'Recipe submitted successfully'


def test_submit_review():
	response = main.app.test_client().post('/submit_review',
		data=json.dumps(dict(user='test', recipe='test', rating=5, review_text='test')),
		content_type='application/json',
	)
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 201
	assert data['message'] == 'Review submitted successfully'


def test_manage_recipes():
	response = main.app.test_client().delete('/manage_recipes',
		data=json.dumps(dict(username='admin', password='admin', recipe='test')),
		content_type='application/json',
	)
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert data['message'] == 'Recipe not found'


def test_remove_inappropriate_content():
	response = main.app.test_client().delete('/remove_inappropriate_content',
		data=json.dumps(dict(username='admin', password='admin', review='test')),
		content_type='application/json',
	)
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert data['message'] == 'Review not found'
