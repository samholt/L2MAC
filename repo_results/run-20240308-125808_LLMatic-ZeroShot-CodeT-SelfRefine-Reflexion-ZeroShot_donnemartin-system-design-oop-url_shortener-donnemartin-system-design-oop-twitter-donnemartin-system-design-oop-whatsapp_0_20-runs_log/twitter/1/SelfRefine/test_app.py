import pytest
import app
import jwt

def test_register():
	app.users = {}
	response = app.register()
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

	response = app.register()
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Username already exists'}

	app.users = {}


def test_login():
	app.users = {'test': {'username': 'test', 'password': 'test'}}
	response = app.login()
	assert response.status_code == 200
	assert 'token' in response.get_json()

	response = app.login()
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}

	app.users = {}

def test_create_post():
	app.users = {'test': {'username': 'test', 'password': 'test'}}
	app.posts = {}
	response = app.create_post()
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created successfully'}

	response = app.create_post()
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid user'}

	app.users = {}
	app.posts = {}

def test_get_posts():
	app.posts = {0: {'user': 'test', 'content': 'test post'}}
	response = app.get_posts()
	assert response.status_code == 200
	assert response.get_json() == app.posts

	app.posts = {}

def test_get_post():
	app.posts = {0: {'user': 'test', 'content': 'test post'}}
	response = app.get_post(0)
	assert response.status_code == 200
	assert response.get_json() == app.posts[0]

	response = app.get_post(1)
	assert response.status_code == 404
	assert response.get_json() == {'message': 'Post not found'}

	app.posts = {}
