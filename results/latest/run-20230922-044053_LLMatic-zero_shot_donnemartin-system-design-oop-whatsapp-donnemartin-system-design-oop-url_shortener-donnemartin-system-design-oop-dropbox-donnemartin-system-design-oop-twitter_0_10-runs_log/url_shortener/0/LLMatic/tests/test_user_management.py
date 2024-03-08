from url_shortener.user_management import create_user, edit_user, delete_user, get_user_urls
from url_shortener.models import User, URL


def test_user_management():
	# Test user creation
	user = create_user('test', 'password')
	assert isinstance(user, User)
	assert user.username == 'test'
	assert user.password == 'password'

	# Test user editing
	edited_user = edit_user(user, 'new_test', 'new_password')
	assert edited_user.username == 'new_test'
	assert edited_user.password == 'new_password'

	# Test user deletion
	delete_user(user)

	# Test retrieval of user's URLs
	urls = get_user_urls(user)
	assert isinstance(urls, list)
