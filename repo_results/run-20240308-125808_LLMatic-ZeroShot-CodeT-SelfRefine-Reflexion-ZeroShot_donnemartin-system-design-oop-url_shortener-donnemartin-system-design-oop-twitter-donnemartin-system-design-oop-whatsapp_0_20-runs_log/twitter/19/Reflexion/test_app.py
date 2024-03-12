import pytest
import app
import jwt


def test_register():
	response = app.register()
	assert response.status_code == 201
	assert response.get_json() == {'message' : 'New user registered!'}


def test_login():
	response = app.login()
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_post():
	response = app.post()
	assert response.status_code == 201
	assert response.get_json() == {'message' : 'New post created!'}


def test_token_required():
	response = app.post()
	assert response.status_code == 401
	assert response.get_json() == {'message' : 'Token is missing!'}


def test_invalid_token():
	app.app.config['SECRET_KEY'] = 'wrongsecret'
	token = jwt.encode({'username' : 'test', 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	app.request.headers['x-access-token'] = token
	response = app.post()
	assert response.status_code == 401
	assert response.get_json() == {'message' : 'Token is invalid!'}
