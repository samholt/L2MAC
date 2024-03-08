from models import User, URL
from datetime import datetime, timedelta


def test_user_model():
	user = User('testuser', 'password')
	assert user.username == 'testuser'
	assert user.password == 'password'
	assert user.urls == []

	url = URL('https://example.com', 'https://short.ly', user, datetime.now(), None)
	user.add_url(url)
	assert url in user.urls

	user.remove_url(url)
	assert url not in user.urls

	User.save_to_db(user)
	assert user in User.users_db.values()

	url2 = URL('https://example2.com', 'https://short.ly/2', user, datetime.now(), None)
	URL.save_to_db(url2)
	assert url2 in URL.urls_db.values()
