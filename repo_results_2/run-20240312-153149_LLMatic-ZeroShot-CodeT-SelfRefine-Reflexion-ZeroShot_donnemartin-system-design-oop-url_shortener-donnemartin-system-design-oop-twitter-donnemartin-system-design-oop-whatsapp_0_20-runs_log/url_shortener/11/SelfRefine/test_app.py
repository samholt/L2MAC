import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		app.DB.clear()
		yield client

@pytest.mark.parametrize('url', [
	'http://example.com',
	'https://google.com',
])
def test_shorten_url(client, url):
	response = client.post('/shorten', json={'url': url})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()

@pytest.mark.parametrize('url, short_url', [
	('http://example.com', 'ABCDE'),
	('https://google.com', '12345'),
])
def test_redirect_url(client, url, short_url):
	app.DB[short_url] = app.URL(url, short_url, 0, datetime.datetime.now(), None, None)
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == url

@pytest.mark.parametrize('short_url', [
	'ABCDE',
	'12345',
])
def test_redirect_url_not_found(client, short_url):
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
	assert 'error' in response.get_json()

@pytest.mark.parametrize('url, short_url', [
	('http://example.com', 'ABCDE'),
	('https://google.com', '12345'),
])
def test_redirect_url_expired(client, url, short_url):
	app.DB[short_url] = app.URL(url, short_url, 0, datetime.datetime.now(), datetime.datetime.now() - datetime.timedelta(days=1), None)
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
	assert 'error' in response.get_json()
