import models


def test_user_model():
	user = models.User('test_user', 'test_password')
	assert user.username == 'test_user'
	assert user.password == 'test_password'


def test_url_model():
	user = models.User('test_user', 'test_password')
	url = models.URL('http://original.com', 'http://short.com', user)
	assert url.original_url == 'http://original.com'
	assert url.shortened_url == 'http://short.com'
	assert url.user == user
	assert url.expiration_date is None


def test_click_model():
	url = models.URL('http://original.com', 'http://short.com', models.User('test_user', 'test_password'))
	click = models.Click(url, '2022-01-01 00:00:00', 'USA')
	assert click.url == url
	assert click.datetime == '2022-01-01 00:00:00'
	assert click.location == 'USA'
