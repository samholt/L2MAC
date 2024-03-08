import pytest
import app
import models
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	user = models.User(id='1', name='Test User', email='test@example.com', urls=[])
	models.db[user.id] = user
	return user

@pytest.fixture
def url(user):
	url = models.URL(original_url='https://example.com', shortened_url='exmpl', user_id=user.id, expiration_date=datetime.datetime.now() + datetime.timedelta(days=1))
	models.db[url.shortened_url] = url
	user.urls.append(url)
	return url


def test_shorten_url(client, user):
	response = client.post('/shorten_url', json={'original_url': 'https://google.com', 'shortened_url': 'goog', 'user_id': user.id, 'expiration_date': (datetime.datetime.now() + datetime.timedelta(days=1)).isoformat()})
	assert response.status_code == 201
	assert models.db['goog'].original_url == 'https://google.com'


def test_redirect_to_url(client, url):
	response = client.get('/' + url.shortened_url)
	assert response.status_code == 302
	assert response.location == url.original_url


def test_user_dashboard(client, user, url):
	response = client.get('/user/' + user.id)
	assert response.status_code == 200
	assert response.get_json() == [url.to_dict()]


def test_admin_dashboard(client, user, url):
	response = client.get('/admin')
	assert response.status_code == 200
	assert response.get_json() == {'users': [user.to_dict()], 'urls': [url.to_dict()]}
