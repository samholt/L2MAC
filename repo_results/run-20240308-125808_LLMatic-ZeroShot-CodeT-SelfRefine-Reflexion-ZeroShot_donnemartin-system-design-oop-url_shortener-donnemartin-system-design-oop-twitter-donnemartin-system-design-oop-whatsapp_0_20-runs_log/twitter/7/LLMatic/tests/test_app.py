import pytest
import app
import jwt
import datetime


def test_register():
	response = app.register()
	assert response[1] == 200


def test_login():
	response = app.login()
	assert response[1] == 200


def test_profile():
	token = jwt.encode({'username': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = app.profile()
	assert response[1] == 200


def test_post():
	token = jwt.encode({'username': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = app.post()
	assert response[1] == 200


def test_search():
	response = app.search()
	assert response[1] == 200


def test_follow():
	token = jwt.encode({'username': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = app.follow('test2')
	assert response[1] == 200


def test_unfollow():
	token = jwt.encode({'username': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = app.unfollow('test2')
	assert response[1] == 200


def test_timeline():
	token = jwt.encode({'username': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = app.timeline()
	assert response[1] == 200


def test_message():
	token = jwt.encode({'username': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = app.message('test2')
	assert response[1] == 200


def test_messages():
	token = jwt.encode({'username': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = app.messages()
	assert response[1] == 200


def test_block():
	token = jwt.encode({'username': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = app.block('test2')
	assert response[1] == 200


def test_notifications():
	token = jwt.encode({'username': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.app.config['SECRET_KEY'])
	response = app.notifications()
	assert response[1] == 200

