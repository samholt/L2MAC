import pytest
from admin import Admin
from database import Database
from user import User
from url_shortener import URLShortener
from datetime import datetime, timedelta

def test_admin():
	admin = Admin()
	user = User()
	url_shortener = URLShortener(Database())

	# Create a user
	user.create_account('test_user', 'password')

	# Create a URL
	short_url = url_shortener.shorten_url('https://www.google.com', datetime.now() + timedelta(days=1))

	# Check that the user and URL are in the system
	assert 'test_user' in admin.db.users
	assert short_url in admin.get_all_urls()

	# Delete the user and URL
	admin.delete_user('test_user')
	admin.delete_url(short_url)

	# Check that the user and URL are no longer in the system
	assert 'test_user' not in admin.db.users
	assert short_url not in admin.get_all_urls()
