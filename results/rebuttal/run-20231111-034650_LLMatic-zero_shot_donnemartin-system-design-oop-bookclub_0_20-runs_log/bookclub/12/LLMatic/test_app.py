import pytest
import app


def test_add_resource():
	app.users['test_user'] = app.User('test_user', 'test@test.com', 'password')
	response = app.app.test_client().post('/resources', json={'username': 'test_user', 'title': 'Test Resource', 'content': 'This is a test resource.'})
	assert response.status_code == 201
	assert 'Test Resource' in app.resources


def test_view_resources():
	response = app.app.test_client().get('/resources')
	assert response.status_code == 200
	assert response.get_json() == {'resources': [{'title': 'Test Resource', 'content': 'This is a test resource.', 'user': 'test_user'}]}


def test_update_resource():
	response = app.app.test_client().put('/resources', json={'username': 'test_user', 'title': 'Test Resource', 'content': 'This is an updated test resource.'})
	assert response.status_code == 200
	assert app.resources['Test Resource'].content == 'This is an updated test resource.'


def test_update_resource_not_authorized():
	response = app.app.test_client().put('/resources', json={'username': 'other_user', 'title': 'Test Resource', 'content': 'This is an unauthorized update.'})
	assert response.status_code == 404
	assert app.resources['Test Resource'].content == 'This is an updated test resource.'

