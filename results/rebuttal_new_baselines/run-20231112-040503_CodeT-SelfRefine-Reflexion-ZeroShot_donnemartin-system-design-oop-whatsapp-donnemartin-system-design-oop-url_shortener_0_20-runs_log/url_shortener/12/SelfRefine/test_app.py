import pytest
import app
from flask import json
from datetime import datetime, timedelta
import sqlite3

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	conn = sqlite3.connect('urls.db')
	c = conn.cursor()
	c.execute('DELETE FROM urls')
	conn.commit()

@pytest.mark.parametrize('url, short_url, user_id, expires_at', [
	('http://example.com', 'exmpl', 'user1', (datetime.now() + timedelta(days=1)).isoformat()),
	('http://google.com', 'goog', 'user2', (datetime.now() + timedelta(days=1)).isoformat()),
])
def test_shorten_url(client, reset_db, url, short_url, user_id, expires_at):
	response = client.post('/shorten', data=json.dumps({'url': url, 'short_url': short_url, 'user_id': user_id, 'expires_at': expires_at}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'short_url': short_url}

	# Test duplicate short URL
	response = client.post('/shorten', data=json.dumps({'url': url, 'short_url': short_url, 'user_id': user_id, 'expires_at': expires_at}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Short URL already in use'}

	# Test invalid URL
	response = client.post('/shorten', data=json.dumps({'url': 'invalid', 'short_url': 'invalid', 'user_id': user_id, 'expires_at': expires_at}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Invalid URL'}

@pytest.mark.parametrize('short_url', ['exmpl', 'goog'])
def test_redirect_url(client, reset_db, short_url):
	app.c.execute('INSERT INTO urls VALUES (?,?,?,?,?,?)', ('http://example.com', short_url, 0, datetime.now().isoformat(), (datetime.now() + timedelta(days=1)).isoformat(), 'user1'))
	app.conn.commit()

	response = client.get(f'/{short_url}')
	assert response.status_code == 302

	# Test expired URL
	app.c.execute('UPDATE urls SET expires_at = ? WHERE shortened = ?', ((datetime.now() - timedelta(days=1)).isoformat(), short_url))
	app.conn.commit()
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'URL not found or expired'}

	# Test non-existent URL
	response = client.get('/nonexistent')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'URL not found or expired'}

@pytest.mark.parametrize('short_url', ['exmpl', 'goog'])
def test_url_info(client, reset_db, short_url):
	app.c.execute('INSERT INTO urls VALUES (?,?,?,?,?,?)', ('http://example.com', short_url, 0, datetime.now().isoformat(), (datetime.now() + timedelta(days=1)).isoformat(), 'user1'))
	app.conn.commit()

	response = client.get(f'/info/{short_url}')
	assert response.status_code == 200
	assert response.get_json() == {'original': 'http://example.com', 'shortened': short_url, 'clicks': 0, 'created_at': datetime.now().isoformat(), 'expires_at': (datetime.now() + timedelta(days=1)).isoformat(), 'user_id': 'user1'}

	# Test non-existent URL
	response = client.get('/info/nonexistent')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'URL not found'}
