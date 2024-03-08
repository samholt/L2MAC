import pytest
from app import app, URL, User, urls_db, users_db
from datetime import datetime, timedelta
import pytz

@pytest.fixture
def sample_url():
	return URL('https://www.google.com', 'abcd', 'user1', 0, datetime.now(pytz.UTC), None)

@pytest.fixture
def sample_user(sample_url):
	return User('user1', [sample_url])

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def setup_db(sample_url, sample_user):
	urls_db[sample_url.short_url] = sample_url
	users_db[sample_user.user_id] = sample_user

@pytest.mark.usefixtures('setup_db')
def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.facebook.com', 'short_url': 'efgh', 'user_id': 'user2'})
	assert response.status_code == 200
	assert urls_db['efgh'].original_url == 'https://www.facebook.com'
	assert urls_db['efgh'].user_id == 'user2'
	assert users_db['user2'].urls[0].short_url == 'efgh'

@pytest.mark.usefixtures('setup_db')
def test_redirect_to_original(client, sample_url):
	response = client.get('/' + sample_url.short_url)
	assert response.status_code == 302
	assert response.location == sample_url.original_url
	assert urls_db[sample_url.short_url].clicks == 1

@pytest.mark.usefixtures('setup_db')
def test_redirect_to_expired_url(client, sample_url):
	sample_url.expires_at = datetime.now(pytz.UTC) - timedelta(days=1)
	response = client.get('/' + sample_url.short_url)
	assert response.status_code == 404
	assert response.get_json() == {'message': 'URL not found or expired'}
