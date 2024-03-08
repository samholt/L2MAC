import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('url, user, expires_at', [
	('https://www.google.com', 'user1', datetime.datetime.now() + datetime.timedelta(days=1)),
	('https://www.example.com', 'user2', datetime.datetime.now() + datetime.timedelta(hours=1)),
])
def test_shorten_url(client, url, user, expires_at):
	response = client.post('/shorten', json={'url': url, 'user': user, 'expires_at': expires_at})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

@pytest.mark.parametrize('short_url', [
	('ABCDE'),
	('12345'),
])
def test_redirect_url(client, short_url):
	response = client.get(f'/{short_url}')
	assert response.status_code in [302, 404]
