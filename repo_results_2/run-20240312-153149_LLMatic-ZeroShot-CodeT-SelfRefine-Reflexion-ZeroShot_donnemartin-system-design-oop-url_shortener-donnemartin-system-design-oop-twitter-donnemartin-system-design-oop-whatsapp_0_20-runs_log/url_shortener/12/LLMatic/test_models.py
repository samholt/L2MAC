import models
from datetime import datetime, timedelta


def test_user_create():
	user = models.User.create(1, 'admin', 'password')
	assert user.id == 1
	assert user.username == 'admin'
	assert user.password == 'password'


def test_user_authenticate():
	user = models.User.create(1, 'admin', 'password')
	assert user.authenticate('admin', 'password')
	assert not user.authenticate('admin', 'wrong_password')


def test_user_get_details():
	user = models.User.create(1, 'admin', 'password')
	assert user.get_details() == {'id': 1, 'username': 'admin', 'password': 'password'}


def test_url_create():
	user = models.User.create(1, 'admin', 'password')
	url = models.URL.create('https://example.com', 'exmpl', user)
	assert url.original_url == 'https://example.com'
	assert url.shortened_url == 'exmpl'
	assert url.user == user
	assert isinstance(url.creation_date, datetime)
	assert isinstance(url.expiration_date, datetime)
	assert url.expiration_date == url.creation_date + timedelta(days=30)


def test_url_get_details():
	user = models.User.create(1, 'admin', 'password')
	url = models.URL.create('https://example.com', 'exmpl', user)
	assert url.get_details() == {
		'original_url': 'https://example.com',
		'shortened_url': 'exmpl',
		'user': user.get_details(),
		'creation_date': url.creation_date.strftime('%Y-%m-%d %H:%M:%S'),
		'expiration_date': url.expiration_date.strftime('%Y-%m-%d %H:%M:%S')
	}


def test_url_delete():
	user = models.User.create(1, 'admin', 'password')
	url = models.URL.create('https://example.com', 'exmpl', user)
	url.delete()
	assert url.original_url is None
	assert url.shortened_url is None
	assert url.user is None
	assert url.creation_date is None
	assert url.expiration_date is None
