import pytest
import views
from models import User, URL
from datetime import datetime, timedelta

# Existing tests...

# New test for URL expiration

def test_url_expiration():
	user = User.create(1, 'test', 'test')
	views.users[user.id] = user
	url = URL('https://www.example.com', 'abc123', user, datetime.now(), datetime.now() - timedelta(days=1))
	views.urls[url.shortened_url] = url
	response = views.app.test_client().get('/abc123')
	assert response.status_code == 410
	assert response.get_json() == {'message': 'URL expired.'}
	assert 'abc123' not in views.urls
