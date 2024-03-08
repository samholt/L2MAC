from flask import Flask
from views import app
import json


def test_create_user_endpoint():
	response = app.test_client().post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert 'message' in data

def test_edit_user_endpoint():
	app.test_client().post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = app.test_client().post('/edit_user', data=json.dumps({'username': 'test', 'new_password': 'new_password'}), content_type='application/json')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert 'message' in data

def test_delete_user_endpoint():
	app.test_client().post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = app.test_client().post('/delete_user', data=json.dumps({'username': 'test'}), content_type='application/json')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert 'message' in data

def test_view_analytics():
	response = app.test_client().get('/analytics/short_url')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert 'clicks' in data
	assert 'click_data' in data

def test_view_all_urls():
	app.test_client().post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	app.test_client().post('/shorten_url', data=json.dumps({'url': 'http://test.com', 'user': 'test'}), content_type='application/json')
	response = app.test_client().get('/admin/urls')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert len(data) == 1

def test_view_all_users():
	app.test_client().post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = app.test_client().get('/admin/users')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert len(data) == 1

def test_delete_url_endpoint():
	app.test_client().post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	app.test_client().post('/shorten_url', data=json.dumps({'url': 'http://test.com', 'user': 'test'}), content_type='application/json')
	response = app.test_client().post('/admin/delete_url', data=json.dumps({'short_url': 'short_url'}), content_type='application/json')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert 'message' in data

def test_view_system_performance():
	app.test_client().post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	app.test_client().post('/shorten_url', data=json.dumps({'url': 'http://test.com', 'user': 'test'}), content_type='application/json')
	response = app.test_client().get('/admin/performance')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert 'total_clicks' in data
	assert 'total_users' in data
	assert 'total_urls' in data

