import pytest
from app import app


def test_register():
	with app.test_client() as c:
		resp = c.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
		assert resp.status_code == 201


def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200


def test_profile():
	with app.test_client() as c:
		resp = c.get('/profile')
		assert resp.status_code == 200
