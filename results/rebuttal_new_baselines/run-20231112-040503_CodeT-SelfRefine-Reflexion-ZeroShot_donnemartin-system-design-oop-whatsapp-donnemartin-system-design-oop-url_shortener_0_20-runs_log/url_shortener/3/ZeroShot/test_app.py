import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user')
	assert response.status_code == 201
	user_id = json.loads(response.data)['user_id']
	assert user_id in app.users


def test_create_url(client):
	user_id = str(app.uuid.uuid4())
	app.users[user_id] = app.User(user_id, {})
	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'user_id': user_id})
	assert response.status_code == 201
	url_id = json.loads(response.data)['url_id']
	assert url_id in app.urls


def test_redirect_url(client):
	user_id = str(app.uuid.uuid4())
	app.users[user_id] = app.User(user_id, {})
	url_id = str(app.uuid.uuid4())
	short_url = url_id[:8]
	app.urls[url_id] = app.URL(url_id, 'https://www.google.com', short_url, user_id, 0, [], None)
	app.users[user_id].urls[url_id] = app.urls[url_id]
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_user_urls(client):
	user_id = str(app.uuid.uuid4())
	app.users[user_id] = app.User(user_id, {})
	response = client.get(f'/user/{user_id}')
	assert response.status_code == 200


def test_get_url_data(client):
	user_id = str(app.uuid.uuid4())
	app.users[user_id] = app.User(user_id, {})
	url_id = str(app.uuid.uuid4())
	short_url = url_id[:8]
	app.urls[url_id] = app.URL(url_id, 'https://www.google.com', short_url, user_id, 0, [], None)
	app.users[user_id].urls[url_id] = app.urls[url_id]
	response = client.get(f'/url/{url_id}')
	assert response.status_code == 200


def test_delete_url(client):
	user_id = str(app.uuid.uuid4())
	app.users[user_id] = app.User(user_id, {})
	url_id = str(app.uuid.uuid4())
	short_url = url_id[:8]
	app.urls[url_id] = app.URL(url_id, 'https://www.google.com', short_url, user_id, 0, [], None)
	app.users[user_id].urls[url_id] = app.urls[url_id]
	response = client.delete(f'/url/{url_id}')
	assert response.status_code == 200
	assert url_id not in app.urls
