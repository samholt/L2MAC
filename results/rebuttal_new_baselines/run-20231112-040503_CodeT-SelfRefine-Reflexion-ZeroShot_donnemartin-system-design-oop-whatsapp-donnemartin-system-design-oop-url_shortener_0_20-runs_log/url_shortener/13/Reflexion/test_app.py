import pytest
import app
import datetime

@pytest.fixture(scope='module')
def setup():
	app.users['test_user'] = app.User('test_user', [])
	app.urls['test_url'] = app.URL('test_url', 'http://original.com', 'http://short.com', 'test_user', 0, [], datetime.datetime.now() + datetime.timedelta(days=1))

@pytest.mark.usefixtures('setup')
def test_create_user():
	response = app.create_user()
	assert response[1] == 400

@pytest.mark.usefixtures('setup')
def test_create_url():
	response = app.create_url()
	assert response[1] == 400

@pytest.mark.usefixtures('setup')
def test_get_url():
	response = app.get_url('test_url')
	assert response[1] == 302

@pytest.mark.usefixtures('setup')
def test_get_user_urls():
	response = app.get_user_urls('test_user')
	assert response[1] == 200
