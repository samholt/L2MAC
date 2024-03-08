from datetime import datetime, timedelta
from models import User, URL, ClickEvent


def test_user_model():
	user = User('test_user', 'test_password')
	assert user.username == 'test_user'
	assert user.password == 'test_password'
	assert user.urls == []


def test_url_model():
	user = User('test_user', 'test_password')
	url = URL('http://test.com', 'http://short.com', user, datetime.now(), datetime.now() + timedelta(days=1))
	assert url.original_url == 'http://test.com'
	assert url.shortened_url == 'http://short.com'
	assert url.user == user
	assert url.click_events == []


def test_click_event_model():
	click_event = ClickEvent(datetime.now(), 'test_location')
	assert click_event.click_time != None
	assert click_event.location == 'test_location'
