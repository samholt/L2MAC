import models

def test_user_model():
	user = models.User(1, 'test', 'password')
	assert user.id == 1
	assert user.username == 'test'
	assert user.password == 'password'

def test_url_model():
	url = models.URL(1, 'http://example.com', 'http://short.com', 1, '2022-12-31')
	assert url.id == 1
	assert url.original_url == 'http://example.com'
	assert url.shortened_url == 'http://short.com'
	assert url.user_id == 1
	assert url.expiration_date == '2022-12-31'

def test_click_model():
	click = models.Click(1, 1, '2022-01-01 00:00:00', 'USA')
	assert click.id == 1
	assert click.url_id == 1
	assert click.timestamp == '2022-01-01 00:00:00'
	assert click.location == 'USA'

