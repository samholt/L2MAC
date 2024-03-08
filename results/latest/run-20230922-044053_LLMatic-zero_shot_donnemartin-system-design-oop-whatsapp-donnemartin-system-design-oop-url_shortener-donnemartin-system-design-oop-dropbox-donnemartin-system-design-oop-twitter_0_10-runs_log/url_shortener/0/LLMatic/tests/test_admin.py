from url_shortener.models import User, URL
from url_shortener.admin import view_all_users, view_all_urls, delete_user, delete_url


def test_view_all_users():
	# Placeholder implementation
	assert len(view_all_users()) == 0


def test_view_all_urls():
	# Placeholder implementation
	assert len(view_all_urls()) == 0


def test_delete_user():
	# Placeholder implementation
	user = User('test', 'test')
	delete_user(user)
	assert user not in view_all_users()


def test_delete_url():
	# Placeholder implementation
	url = URL('https://example.com', 'https://short.ly', User('test', 'test'))
	delete_url(url)
	assert url not in view_all_urls()
