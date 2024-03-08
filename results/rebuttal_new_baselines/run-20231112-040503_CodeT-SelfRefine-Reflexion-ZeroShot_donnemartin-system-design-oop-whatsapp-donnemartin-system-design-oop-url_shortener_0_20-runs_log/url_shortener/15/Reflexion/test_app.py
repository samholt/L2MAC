import pytest
from app import app, User, Url, users, urls
from datetime import datetime, timedelta
import pytz

@pytest.fixture
def sample_user():
	return User('test_user', 'password', {})

@pytest.fixture
def sample_url():
	return Url('https://www.google.com', 'google', datetime.now(pytz.UTC) + timedelta(days=1), 0, [])

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_shorten_url(client, sample_user, sample_url):
	users[sample_user.username] = sample_user
	response = client.post('/shorten_url', json={'username': sample_user.username, 'original_url': sample_url.original_url, 'short_url': sample_url.short_url, 'expiration_date': sample_url.expiration_date.strftime('%Y-%m-%d %H:%M:%S')})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'URL shortened successfully'}
	assert sample_url.short_url in users[sample_user.username].urls
	assert sample_url.short_url in urls


def test_redirect_url(client, sample_user, sample_url):
	users[sample_user.username] = sample_user
	users[sample_user.username].urls[sample_url.short_url] = sample_url
	urls[sample_url.short_url] = sample_url
	response = client.get('/' + sample_url.short_url)
	assert response.status_code == 302
	assert users[sample_user.username].urls[sample_url.short_url].clicks == 1


def test_redirect_expired_url(client, sample_user, sample_url):
	sample_url.expiration_date = datetime.now(pytz.UTC) - timedelta(days=1)
	users[sample_user.username] = sample_user
	users[sample_user.username].urls[sample_url.short_url] = sample_url
	urls[sample_url.short_url] = sample_url
	response = client.get('/' + sample_url.short_url)
	assert response.status_code == 410
	assert response.get_json() == {'message': 'URL expired'}
	assert users[sample_user.username].urls[sample_url.short_url].clicks == 0
