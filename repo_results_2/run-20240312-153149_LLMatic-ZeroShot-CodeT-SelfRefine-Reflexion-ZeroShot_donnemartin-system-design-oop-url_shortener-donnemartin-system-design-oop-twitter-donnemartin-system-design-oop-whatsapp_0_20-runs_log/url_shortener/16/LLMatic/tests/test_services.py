import services
from models import URL, Click, User
from datetime import datetime, timedelta


def test_generate_short_link():
	url = 'https://www.google.com'
	shortened_url = services.generate_short_link(url)
	assert shortened_url.original_url == url
	assert len(shortened_url.shortened_url) == 6


def test_get_original_url():
	url = 'https://www.google.com'
	shortened_url = services.generate_short_link(url)
	original_url = services.get_original_url(shortened_url.shortened_url)
	assert original_url == url


def test_record_click():
	url = 'https://www.google.com'
	location = '127.0.0.1'
	click = services.record_click(url, location)
	assert click.url == url
	assert click.location == location


def test_get_clicks():
	url = 'https://www.google.com'
	location = '127.0.0.1'
	services.record_click(url, location)
	clicks = services.get_clicks(url)
	assert len(clicks) == 1
	assert clicks[0].url == url
	assert clicks[0].location == location


def test_create_user():
	username = 'test'
	password = 'password'
	user = services.create_user(username, password)
	assert user.username == username
	assert user.password == password


def test_get_user():
	username = 'test'
	password = 'password'
	services.create_user(username, password)
	user = services.get_user(username)
	assert user.username == username
	assert user.password == password


def test_edit_user():
	username = 'test'
	password = 'password'
	new_password = 'new_password'
	services.create_user(username, password)
	user = services.edit_user(username, new_password)
	assert user.username == username
	assert user.password == new_password


def test_delete_user():
	username = 'test'
	password = 'password'
	services.create_user(username, password)
	message = services.delete_user(username)
	assert message == 'User deleted'
	user = services.get_user(username)
	assert user is None


def test_get_all_urls():
	url1 = 'https://www.google.com'
	url2 = 'https://www.facebook.com'
	services.generate_short_link(url1)
	services.generate_short_link(url2)
	urls = services.get_all_urls()
	assert len(urls) == 2


def test_delete_url():
	url = 'https://www.google.com'
	shortened_url = services.generate_short_link(url)
	message = services.delete_url(shortened_url.shortened_url)
	assert message == 'URL deleted'
	url = services.get_original_url(shortened_url.shortened_url)
	assert url is None


def test_get_all_users():
	username1 = 'test1'
	password1 = 'password1'
	username2 = 'test2'
	password2 = 'password2'
	services.create_user(username1, password1)
	services.create_user(username2, password2)
	users = services.get_all_users()
	assert len(users) == 2
