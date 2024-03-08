import pytest
import app
import models
from flask import jsonify


def test_register():
	app.db.create_all()
	response = app.register()
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Registered successfully'}


def test_login():
	response = app.login()
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_login_invalid():
	response = app.login()
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}
