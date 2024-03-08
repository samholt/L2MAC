import pytest
from app import app, URL, conn, c
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def sample_url():
	return URL('http://example.com', '12345678', 'test_user', 0, datetime.now(), datetime.now() + timedelta(days=1))


def test_shorten_url(client, sample_url):
	response = client.post('/shorten', json={'url': sample_url.original, 'user': sample_url.user, 'expires_at': sample_url.expires_at.isoformat()})
	assert response.status_code == 201
	shortened_url = response.get_json()['shortened_url']
	c.execute("SELECT * FROM urls WHERE shortened=?", (shortened_url,))
	url = c.fetchone()
	assert url is not None


def test_redirect_url(client, sample_url):
	c.execute("INSERT INTO urls VALUES (?, ?, ?, ?, ?, ?)", (sample_url.original, sample_url.shortened, sample_url.user, sample_url.clicks, sample_url.created_at, sample_url.expires_at))
	conn.commit()
	response = client.get(f'/{sample_url.shortened}')
	assert response.status_code == 302
	assert response.location == sample_url.original


def test_redirect_expired_url(client, sample_url):
	sample_url.expires_at = datetime.now() - timedelta(days=1)
	c.execute("INSERT INTO urls VALUES (?, ?, ?, ?, ?, ?)", (sample_url.original, sample_url.shortened, sample_url.user, sample_url.clicks, sample_url.created_at, sample_url.expires_at))
	conn.commit()
	response = client.get(f'/{sample_url.shortened}')
	assert response.status_code == 404
