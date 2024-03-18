from shortener import URLShortener
from models import User


def test_url_shortener():
	shortener = URLShortener()
	assert shortener.users == {}
	assert shortener.urls == {}

	user = shortener.create_user('test', 'password')
	assert isinstance(user, User)
	assert shortener.users == {'test': user}

	url = shortener.create_url('http://google.com', user)
	assert url in shortener.urls.values()
	assert url in user.urls.values()

	shortener.delete_url(url.shortened_url, user)
	assert url not in shortener.urls.values()
	assert url not in user.urls.values()
