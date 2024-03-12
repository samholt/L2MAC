import datetime
from models import User, URL, ClickEvent

def test_user_model():
	user = User('test_user', 'test_password')
	assert user.username == 'test_user'
	assert user.password == 'test_password'
	assert user.urls == []

def test_url_model():
	user = User('test_user', 'test_password')
	url = URL('http://example.com', 'http://short.url', user, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=1))
	assert url.original_url == 'http://example.com'
	assert url.shortened_url == 'http://short.url'
	assert url.user == user
	assert url.click_events == []

def test_click_event_model():
	click_event = ClickEvent(datetime.datetime.now(), 'USA')
	assert click_event.date_time is not None
	assert click_event.location == 'USA'
