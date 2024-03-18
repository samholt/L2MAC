import pytest
from flask import Flask
import app
from url_shortener import url_database, generate_short_url
from user_accounts import User, users

def test_home():
	with app.app.test_client() as c:
		resp = c.get('/')
		assert resp.data == b'Hello, World!'

def test_redirect_to_url():
	url = 'http://example.com'
	short_url = generate_short_url(url)
	with app.app.test_client() as c:
		resp = c.get('/' + short_url)
		assert resp.status_code == 302
		assert resp.location == url

		resp = c.get('/nonexistent')
		assert resp.status_code == 404

def test_admin_view_all_urls():
	User.register('test_user', 'password')
	User.add_url('test_user', 'short', 'http://example.com')
	with app.app.test_client() as c:
		resp = c.get('/admin/view_all_urls')
		assert resp.status_code == 200
		assert resp.json == {'urls': {'test': {'short': 'long'}, 'test_user': {'short': 'http://example.com'}}}

def test_admin_delete_user():
	User.register('test_user', 'password')
	with app.app.test_client() as c:
		resp = c.delete('/admin/delete_user/test_user')
		assert resp.status_code == 200
		assert resp.json == {'success': True}
		assert 'test_user' not in users.keys()

