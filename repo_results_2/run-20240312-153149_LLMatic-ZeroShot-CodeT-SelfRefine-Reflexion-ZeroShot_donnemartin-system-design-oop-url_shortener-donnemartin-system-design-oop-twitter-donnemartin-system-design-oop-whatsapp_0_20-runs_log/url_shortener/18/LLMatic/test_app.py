import pytest
from flask import json
from app import app


def test_create_user():
	with app.test_client() as c:
		resp = c.post('/create_user', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 201
		assert json.loads(resp.data) == {'message': 'User created successfully'}


def test_edit_user():
	with app.test_client() as c:
		resp = c.put('/edit_user', json={'username': 'test', 'password': 'new_password'})
		assert resp.status_code == 200
		assert json.loads(resp.data) == {'message': 'User updated successfully'}


def test_delete_user():
	with app.test_client() as c:
		resp = c.delete('/delete_user', json={'username': 'test'})
		assert resp.status_code == 200
		assert json.loads(resp.data) == {'message': 'User deleted successfully'}


def test_create_url():
	with app.test_client() as c:
		resp = c.post('/create_user', json={'username': 'test', 'password': 'test'})
		resp = c.post('/create_url', json={'original_url': 'http://example.com', 'username': 'test'})
		assert resp.status_code == 201
		assert 'short_url' in json.loads(resp.data)


def test_redirect():
	with app.test_client() as c:
		resp = c.post('/create_user', json={'username': 'test', 'password': 'test'})
		resp = c.post('/create_url', json={'original_url': 'http://example.com', 'username': 'test'})
		short_url = json.loads(resp.data)['short_url']
		resp = c.get(f'/{short_url}')
		assert resp.status_code == 302
		assert json.loads(resp.data) == {'redirect': 'http://example.com'}


def test_view_analytics():
	with app.test_client() as c:
		resp = c.post('/create_user', json={'username': 'test', 'password': 'test'})
		resp = c.post('/create_url', json={'original_url': 'http://example.com', 'username': 'test'})
		short_url = json.loads(resp.data)['short_url']
		c.get(f'/{short_url}')
		resp = c.get('/view_analytics', json={'username': 'test'})
		assert resp.status_code == 200
		assert short_url in json.loads(resp.data)


def test_admin_view_all_urls():
	with app.test_client() as c:
		resp = c.get('/admin/view_all_urls')
		assert resp.status_code == 200


def test_admin_delete_url():
	with app.test_client() as c:
		resp = c.post('/create_user', json={'username': 'test', 'password': 'test'})
		resp = c.post('/create_url', json={'original_url': 'http://example.com', 'username': 'test'})
		short_url = json.loads(resp.data)['short_url']
		resp = c.delete('/admin/delete_url', json={'short_url': short_url})
		assert resp.status_code == 200
		assert json.loads(resp.data) == {'message': 'URL deleted successfully'}


def test_admin_delete_user():
	with app.test_client() as c:
		resp = c.post('/create_user', json={'username': 'test', 'password': 'test'})
		resp = c.delete('/admin/delete_user', json={'username': 'test'})
		assert resp.status_code == 200
		assert json.loads(resp.data) == {'message': 'User deleted successfully'}


def test_admin_monitor_system():
	with app.test_client() as c:
		resp = c.get('/admin/monitor_system')
		assert resp.status_code == 200
		assert 'user_count' in json.loads(resp.data)
		assert 'url_count' in json.loads(resp.data)
