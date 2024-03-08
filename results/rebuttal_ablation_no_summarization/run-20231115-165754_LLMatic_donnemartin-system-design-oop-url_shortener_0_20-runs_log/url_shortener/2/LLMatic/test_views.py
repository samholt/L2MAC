import pytest
from views import app, urls
from models import User, URL
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_redirect_to_url(client):
	# Test redirection to original URL
	user = User('test', 'test')
	url = URL('http://original.com', 'short', user)
	urls['short'] = url
	response = client.get('/short')
	assert response.status_code == 302
	assert response.location == 'http://original.com'

	# Test URL expiration
	expired_url = URL('http://expired.com', 'expired', user, datetime.now() - timedelta(days=1))
	urls['expired'] = expired_url
	response = client.get('/expired')
	assert response.status_code == 410
	assert response.data == b'URL expired'
