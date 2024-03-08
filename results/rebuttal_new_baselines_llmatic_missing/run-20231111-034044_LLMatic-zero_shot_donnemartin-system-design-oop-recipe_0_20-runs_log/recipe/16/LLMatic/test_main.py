import pytest
from main import app
from flask import json


def test_register():
	with app.test_client() as c:
		resp = c.post('/register', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['username'] == 'test'
		assert data['password'] == 'test'


def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['username'] == 'test'
		assert data['password'] == 'test'


def test_logout():
	with app.test_client() as c:
		resp = c.post('/logout', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['username'] == 'test'


def test_create_recipe():
	with app.test_client() as c:
		resp = c.post('/recipe', json={'name': 'test', 'ingredients': ['test'], 'instructions': 'test', 'images': ['test'], 'categories': ['test'], 'user_ratings': {'test': 5}})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['name'] == 'test'
		assert data['ingredients'] == ['test']
		assert data['instructions'] == 'test'
		assert data['images'] == ['test']
		assert data['categories'] == ['test']
		assert data['user_ratings'] == {'test': 5}


def test_view_recipe():
	with app.test_client() as c:
		resp = c.get('/recipe', json={'name': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['name'] == 'test'


def test_edit_recipe():
	with app.test_client() as c:
		resp = c.put('/recipe', json={'name': 'test', 'new_name': 'test2'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['name'] == 'test2'


def test_delete_recipe():
	with app.test_client() as c:
		resp = c.delete('/recipe', json={'name': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['name'] == 'test'


def test_create_review():
	with app.test_client() as c:
		resp = c.post('/review', json={'user': 'test', 'recipe': 'test', 'rating': 5, 'text': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['user'] == 'test'
		assert data['recipe'] == 'test'
		assert data['rating'] == 5
		assert data['text'] == 'test'


def test_view_review():
	with app.test_client() as c:
		resp = c.get('/review', json={'id': 1})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['id'] == 1


def test_edit_review():
	with app.test_client() as c:
		resp = c.put('/review', json={'id': 1, 'new_text': 'test2'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['text'] == 'test2'


def test_delete_review():
	with app.test_client() as c:
		resp = c.delete('/review', json={'id': 1})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['id'] == 1


def test_create_category():
	with app.test_client() as c:
		resp = c.post('/category', json={'name': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['name'] == 'test'


def test_view_category():
	with app.test_client() as c:
		resp = c.get('/category', json={'name': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['name'] == 'test'


def test_edit_category():
	with app.test_client() as c:
		resp = c.put('/category', json={'name': 'test', 'new_name': 'test2'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['name'] == 'test2'


def test_delete_category():
	with app.test_client() as c:
		resp = c.delete('/category', json={'name': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['name'] == 'test'


def test_admin_action():
	with app.test_client() as c:
		resp = c.post('/admin', json={'username': 'test', 'password': 'test', 'action': 'delete', 'target': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['username'] == 'test'
		assert data['password'] == 'test'
		assert data['action'] == 'delete'
		assert data['target'] == 'test'


def test_search():
	with app.test_client() as c:
		resp = c.get('/search', json={'query': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert 'test' in data


def test_recommendation():
	with app.test_client() as c:
		resp = c.get('/recommendation', json={'username': 'test'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert 'test' in data


def test_community_action():
	with app.test_client() as c:
		resp = c.post('/community', json={'username': 'test', 'action': 'share', 'target': 'test', 'platform': 'Facebook'})
		assert resp.status_code == 200
		data = json.loads(resp.data.decode())
		assert data['username'] == 'test'
		assert data['action'] == 'share'
		assert data['target'] == 'test'
		assert data['platform'] == 'Facebook'
