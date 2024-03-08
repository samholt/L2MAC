from models import User, URL, Click

def test_user_model():
	user = User(id=1, username='test', password='test', urls=[])
	assert user.id == 1
	assert user.username == 'test'
	assert user.password == 'test'
	assert user.urls == []

def test_url_model():
	url = URL(id=1, original_url='http://test.com', shortened_url='http://short.com', user_id=1, clicks=[], expiration_date='2022-12-31')
	assert url.id == 1
	assert url.original_url == 'http://test.com'
	assert url.shortened_url == 'http://short.com'
	assert url.user_id == 1
	assert url.clicks == []
	assert url.expiration_date == '2022-12-31'

def test_click_model():
	click = Click(id=1, url_id=1, click_time='2022-01-01 00:00:00', click_location='USA')
	assert click.id == 1
	assert click.url_id == 1
	assert click.click_time == '2022-01-01 00:00:00'
	assert click.click_location == 'USA'
