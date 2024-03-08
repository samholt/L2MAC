import pytest
import app
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def url():
	return app.URL('https://www.google.com', '12345678', 'test_user', 0, datetime.now(), datetime.now() + timedelta(days=1))


def test_shorten_url(client, url):
	response = client.post('/shorten', json={'url': url.original, 'user': url.user, 'expires_at': url.expires_at.strftime('%Y-%m-%d %H:%M:%S')})
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()


def test_redirect_url(client, url):
	app.c.execute("INSERT INTO urls VALUES (?, ?, ?, ?, ?, ?)", (url.original, url.shortened, url.user, url.clicks, url.created_at, url.expires_at))
	app.conn.commit()
	response = client.get(f'/{url.shortened}')
	assert response.status_code == 302
	assert app.c.execute("SELECT clicks FROM urls WHERE shortened = ?", (url.shortened,)).fetchone()[0] == 1


def test_redirect_url_not_found(client):
	response = client.get('/notfound')
	assert response.status_code == 404
	assert 'error' in response.get_json()


def test_redirect_url_expired(client, url):
	url.expires_at = datetime.now() - timedelta(days=1)
	app.c.execute("INSERT INTO urls VALUES (?, ?, ?, ?, ?, ?)", (url.original, url.shortened, url.user, url.clicks, url.created_at, url.expires_at))
	app.conn.commit()
	response = client.get(f'/{url.shortened}')
	assert response.status_code == 404
	assert 'error' in response.get_json()
