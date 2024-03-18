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
	return app.URL(original='https://www.google.com', short='ABCDE', clicks=0, created_at=datetime.datetime.now(), expires_at=None, user_id='user1')


def test_shorten_url(client, sample_url):
	response = client.post('/shorten', json={'url': sample_url.original, 'user_id': sample_url.user_id})
	assert response.status_code == 201
	short_url = response.get_json()['short_url']
	assert short_url in app.DB


def test_redirect_url(client, sample_url):
	app.DB[sample_url.short] = sample_url
	response = client.get(f'/{sample_url.short}')
	assert response.status_code == 302
	assert response.location == sample_url.original


def test_redirect_url_not_found(client):
	response = client.get('/NOTFOUND')
	assert response.status_code == 404


def test_redirect_url_expired(client, sample_url):
	sample_url.expires_at = datetime.datetime.now() - datetime.timedelta(days=1)
	app.DB[sample_url.short] = sample_url
	response = client.get(f'/{sample_url.short}')
	assert response.status_code == 404
