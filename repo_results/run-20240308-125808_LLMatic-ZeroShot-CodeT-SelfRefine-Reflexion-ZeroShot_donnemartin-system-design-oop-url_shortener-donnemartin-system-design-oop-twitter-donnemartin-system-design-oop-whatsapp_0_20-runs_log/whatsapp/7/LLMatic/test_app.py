import pytest
import time
import app
from flask import json


def test_create_user():
	with app.app.test_request_context(json={'email': 'test@test.com', 'password': 'test'}):
		response = app.create_user()
		assert response == ({'message': 'User created'}, 201)


def test_get_user():
	with app.app.test_request_context(json={'email': 'test@test.com', 'password': 'test'}):
		app.create_user()
		response = app.get_user('test@test.com')
		assert response[0]['email'] == 'test@test.com'
		assert response[0]['online'] == True


def test_update_connectivity():
	with app.app.test_request_context(json={'email': 'test@test.com', 'password': 'test'}):
		app.create_user()
		with app.app.test_request_context(json={'online': False}):
			response = app.update_connectivity('test@test.com')
			assert response == ({'message': 'Connectivity updated'}, 200)
			response = app.get_user('test@test.com')
			assert response[0]['online'] == False


def test_post_status():
	with app.app.test_request_context(json={'email': 'test@test.com', 'password': 'test'}):
		app.create_user()
		with app.app.test_request_context(json={'email': 'test@test.com', 'status': 'Hello, world!'}):
			response = app.post_status()
			assert response[0]['message'] == 'Status posted'
			response = app.get_user('test@test.com')
			assert response[0]['statuses'][0]['status'] == 'Hello, world!'


def test_offline_queue():
	with app.app.test_request_context(json={'email': 'test@test.com', 'password': 'test'}):
		app.create_user()
		with app.app.test_request_context(json={'online': False}):
			app.update_connectivity('test@test.com')
			with app.app.test_request_context(json={'email': 'test@test.com', 'status': 'Hello, world!'}):
				response = app.post_status()
				assert response[0]['message'] == 'User is offline, status added to queue'
				time.sleep(5)
				with app.app.test_request_context(json={'online': True}):
					app.update_connectivity('test@test.com')
					response = app.get_user('test@test.com')
					assert response[0]['statuses'][0]['status'] == 'Hello, world!'

