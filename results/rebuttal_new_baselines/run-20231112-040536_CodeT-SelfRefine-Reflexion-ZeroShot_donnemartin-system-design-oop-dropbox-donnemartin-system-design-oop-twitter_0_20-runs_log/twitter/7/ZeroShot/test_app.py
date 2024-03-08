import pytest
import app
import jwt

def test_register():
	app.users = {}
	response = app.register()
	assert response[1] == 200

	data = response[0].get_json()
	assert data['message'] == 'Registered successfully'

	assert 'test' in app.users

	user = app.users['test']
	assert user.username == 'test'
	assert user.email == 'test@test.com'
	assert user.password == 'test'
	assert user.profile == {}


def test_login():
	app.users = {'test': app.User('test', 'test@test.com', 'test', {})}
	response = app.login()
	assert response[1] == 200

	data = response[0].get_json()
	assert 'token' in data

	decoded = jwt.decode(data['token'], app.SECRET_KEY)
	assert decoded['user'] == 'test'


def test_post():
	app.users = {'test': app.User('test', 'test@test.com', 'test', {})}
	app.posts = {}
	response = app.post()
	assert response[1] == 200

	data = response[0].get_json()
	assert data['message'] == 'Posted successfully'

	assert len(app.posts) == 1

	post = app.posts[0]
	assert post.user == 'test'
	assert post.content == 'Hello, world!'
	assert post.likes == 0
	assert post.retweets == 0
	assert post.replies == []
