import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_url():
	return app.URL('http://example.com', 'ABCDE', 0, datetime.datetime.now(), None, None)


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'http://example.com', 'expires_at': None, 'owner': None})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_shorten_url_without_url(client):
	response = client.post('/shorten', json={'expires_at': None, 'owner': None})
	assert response.status_code == 400


def test_redirect_url(client, sample_url):
	app.DB[sample_url.shortened] = sample_url
	response = client.get(f'/{sample_url.shortened}')
	assert response.status_code == 302
	assert app.DB[sample_url.shortened].clicks == 1


def test_redirect_url_not_found(client):
	response = client.get('/NOTFOUND')
	assert response.status_code == 404


def test_redirect_url_expired(client, sample_url):
	sample_url.expires_at = datetime.datetime.now() - datetime.timedelta(days=1)
	app.DB[sample_url.shortened] = sample_url
	response = client.get(f'/{sample_url.shortened}')
	assert response.status_code == 404
