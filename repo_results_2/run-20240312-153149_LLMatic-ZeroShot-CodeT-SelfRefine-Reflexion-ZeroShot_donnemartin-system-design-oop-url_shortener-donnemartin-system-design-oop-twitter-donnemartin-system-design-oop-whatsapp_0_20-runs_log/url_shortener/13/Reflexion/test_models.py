from models import User, URL


def test_user():
	user = User('test', 'password')
	assert user.username == 'test'
	assert user.password == 'password'
	assert user.urls == {}

	user.add_url('http://google.com', 'abcd')
	assert user.urls == {'abcd': 'http://google.com'}

	user.delete_url('abcd')
	assert user.urls == {}


def test_url():
	user = User('test', 'password')
	url = URL('http://google.com', 'abcd', user)
	assert url.original_url == 'http://google.com'
	assert url.shortened_url == 'abcd'
	assert url.user == user
	assert url.clicks == []
	assert url.expiration_date is None

	url.add_click({'ip': '127.0.0.1', 'time': '2021-01-01T00:00:00Z'})
	assert url.clicks == [{'ip': '127.0.0.1', 'time': '2021-01-01T00:00:00Z'}]

	assert url.is_expired() is False
