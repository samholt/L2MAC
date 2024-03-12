import pytest
from app import app
from flask import json


def test_register():
	with app.test_client() as c:
		resp = c.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
		assert resp.get_json() == {'message': 'User registered successfully'}


def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
		assert resp.get_json() == {'message': 'Login successful'}


def test_profile():
	with app.test_client() as c:
		resp = c.post('/profile', json={'email': 'test@test.com', 'profile_picture': 'pic.jpg', 'status_message': 'Hello', 'privacy_setting': 'public'})
		assert resp.get_json() == {'message': 'Profile updated'}
		resp = c.get('/profile', json={'email': 'test@test.com'})
		assert resp.get_json() == {'email': 'test@test.com', 'profile_picture': 'pic.jpg', 'status_message': 'Hello', 'privacy_setting': 'public'}


def test_contact():
	with app.test_client() as c:
		resp = c.post('/contact', json={'name': 'John'})
		assert resp.get_json() == {'message': 'Contact created'}


def test_message():
	with app.test_client() as c:
		resp = c.post('/message', json={'sender': 'test@test.com', 'receiver': 'john@test.com', 'content': 'Hello John'})
		assert resp.get_json() == {'message': 'Message sent'}


def test_group():
	with app.test_client() as c:
		resp = c.post('/group', json={'group_name': 'Test Group', 'admin': 'test@test.com'})
		assert resp.get_json() == {'message': 'Group created'}


def test_status():
	with app.test_client() as c:
		resp = c.post('/status', json={'email': 'test@test.com', 'content': 'Hello World', 'visibility_duration': '1 day', 'visibility_setting': 'public'})
		assert resp.get_json() == {'message': 'Status posted'}

