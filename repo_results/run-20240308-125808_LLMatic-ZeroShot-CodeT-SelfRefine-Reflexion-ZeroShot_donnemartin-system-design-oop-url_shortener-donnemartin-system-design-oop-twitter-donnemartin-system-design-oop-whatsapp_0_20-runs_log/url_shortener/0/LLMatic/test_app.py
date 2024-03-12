import pytest
import app
import url_shortener as us


def test_home():
	response = app.home()
	assert response == 'Hello, World!'

def test_generate_url():
	app.app.testing = True
	client = app.app.test_client()
	response = client.post('/generate', data={'url': 'http://example.com'})
	assert response.status_code == 200
	assert len(response.data.decode()) == 6

def test_custom_url():
	app.app.testing = True
	client = app.app.test_client()
	response = client.post('/custom', data={'url': 'http://example.com', 'custom_link': 'custom'})
	assert response.status_code == 200
	assert response.data.decode() == 'custom'

def test_analytics():
	us.DATABASE['test'] = 'http://example.com'
	response = app.analytics('test')
	assert response == []

def test_create_account():
	app.app.testing = True
	client = app.app.test_client()
	response = client.post('/account/create', data={'username': 'test', 'password': 'password'})
	assert response.status_code == 200
	assert response.data.decode() == 'Account created successfully.'

def test_view_urls():
	response = app.view_urls('test')
	assert response == []

def test_view_all_urls():
	response = app.view_all_urls()
	assert response == us.DATABASE
