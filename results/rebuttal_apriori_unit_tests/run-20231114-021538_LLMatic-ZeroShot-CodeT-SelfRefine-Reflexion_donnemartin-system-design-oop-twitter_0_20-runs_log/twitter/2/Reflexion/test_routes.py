import pytest
import app.routes
from flask import json


def test_register():
	with app.test_request_context('/register', method='POST'):
		# check that post data gets processed
		response = app.routes.register()
		data = json.loads(response.get_data(as_text=True))
		assert response.status_code == 201
		assert 'message' in data
		assert data['message'] == 'Registered successfully'


def test_login():
	with app.test_request_context('/login', method='POST'):
		# check that post data gets processed
		response = app.routes.login()
		data = json.loads(response.get_data(as_text=True))
		if response.status_code == 200:
			assert 'token' in data
		else:
			assert 'message' in data
			assert data['message'] == 'Invalid username or password'
