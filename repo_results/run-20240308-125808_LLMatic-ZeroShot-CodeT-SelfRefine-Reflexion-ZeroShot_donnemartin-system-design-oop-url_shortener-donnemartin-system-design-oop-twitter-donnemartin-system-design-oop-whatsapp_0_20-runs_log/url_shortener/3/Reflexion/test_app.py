import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('url, user, expires_at', [
	('http://example.com', 'user1', datetime.datetime.now() + datetime.timedelta(days=1)),
	('http://google.com', 'user2', datetime.datetime.now() + datetime.timedelta(hours=1))
])
def test_shorten_url(client, url, user, expires_at):
	response = client.post('/shorten', json={'url': url, 'user': user, 'expires_at': expires_at.isoformat()})
	assert response.status_code == 201
	short_url = response.get_json()['short_url']
	assert short_url in app.urls
	assert app.urls[short_url].original == url
	assert app.urls[short_url].user == user
	assert app.urls[short_url].expires_at == expires_at

@pytest.mark.parametrize('short_url', ['ABCDE', '12345'])
def test_redirect_url(client, short_url):
	response = client.get(f'/{short_url}')
	if short_url in app.urls and app.urls[short_url].expires_at > datetime.datetime.now():
		assert response.status_code == 302
		assert response.location == app.urls[short_url].original
	else:
		assert response.status_code == 404
