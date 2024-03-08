import sys
sys.path.append('../')

from url_shortener.models import User, URL, Click
from datetime import datetime

def test_user_model():
	user = User('test_user', 'test_password')
	assert user.username == 'test_user'
	assert user.password == 'test_password'

def test_url_model():
	user = User('test_user', 'test_password')
	url = URL('http://test.com', 'http://short.com', user, datetime.now())
	assert url.original_url == 'http://test.com'
	assert url.shortened_url == 'http://short.com'
	assert url.user == user

def test_click_model():
	user = User('test_user', 'test_password')
	url = URL('http://test.com', 'http://short.com', user, datetime.now())
	click = Click(url, datetime.now(), 'USA')
	assert click.url == url
	assert click.location == 'USA'
