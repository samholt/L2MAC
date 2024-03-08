import pytest
from flask import json
from app import app


def test_signup():
	with app.test_client() as c:
		response = c.post('/signup', json={'email': 'test@test.com', 'password': 'password'})
		data = json.loads(response.get_data(as_text=True))
		assert data == 'User created successfully'

		response = c.post('/signup', json={'email': 'test@test.com', 'password': 'password'})
		data = json.loads(response.get_data(as_text=True))
		assert data == 'User already exists'


def test_login():
	with app.test_client() as c:
		response = c.post('/login', json={'email': 'test@test.com', 'password': 'password'})
		data = json.loads(response.get_data(as_text=True))
		assert data == 'Logged in successfully'


def test_recover():
	with app.test_client() as c:
		response = c.post('/recover', json={'email': 'test@test.com'})
		data = json.loads(response.get_data(as_text=True))
		assert data == 'password'


def test_send_message():
	with app.test_client() as c:
		response = c.post('/send_message', json={'sender': 'test@test.com', 'receiver': 'test2@test.com', 'content': 'Hello'})
		data = json.loads(response.get_data(as_text=True))
		assert data == 'Message queued'

