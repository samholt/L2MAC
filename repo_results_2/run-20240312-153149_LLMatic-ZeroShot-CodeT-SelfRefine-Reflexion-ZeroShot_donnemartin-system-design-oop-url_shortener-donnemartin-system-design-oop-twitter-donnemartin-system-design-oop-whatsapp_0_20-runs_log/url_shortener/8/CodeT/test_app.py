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
	return app.URL(original='https://www.google.com', short='ABCDE', clicks=0, created_at=datetime.datetime.now(), expires_at=datetime.datetime.now() + datetime.timedelta(days=30))


def test_shorten_url(client, sample_url):
	response = client.post('/shorten', json={'url': sample_url.original})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_url(client, sample_url):
	app.DB[sample_url.short] = sample_url
	response = client.get(f'/{sample_url.short}')
	assert response.status_code == 302
	assert app.DB[sample_url.short].clicks == 1


def test_redirect_url_not_found_or_expired(client):
	response = client.get('/NOTFOUND')
	assert response.status_code == 404
