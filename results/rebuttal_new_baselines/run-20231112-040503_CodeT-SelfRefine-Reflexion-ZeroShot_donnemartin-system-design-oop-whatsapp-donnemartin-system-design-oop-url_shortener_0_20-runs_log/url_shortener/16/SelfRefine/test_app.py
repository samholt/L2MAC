import pytest
import app
from flask import json
from contextlib import closing

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user')
	assert response.status_code == 201
	user_id = json.loads(response.data)['user_id']
	with closing(app.sqlite3.connect(app.DATABASE)) as db:
		with closing(db.cursor()) as cursor:
			cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
			user = cursor.fetchone()
	assert user is not None


def test_shorten_url(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	assert response.status_code == 201
	short_url = json.loads(response.data)['short_url']
	with closing(app.sqlite3.connect(app.DATABASE)) as db:
		with closing(db.cursor()) as cursor:
			cursor.execute("SELECT * FROM urls WHERE short_url = ?", (short_url,))
			url = cursor.fetchone()
	assert url is not None


def test_redirect_url(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	client.get(f'/{short_url}')
	response = client.get('/analytics', json={'user_id': user_id})
	assert response.status_code == 200
	analytics = json.loads(response.data)
	with closing(app.sqlite3.connect(app.DATABASE)) as db:
		with closing(db.cursor()) as cursor:
			cursor.execute("SELECT * FROM urls WHERE short_url = ?", (short_url,))
			url = cursor.fetchone()
	assert analytics[short_url]['clicks'] == url[4]
