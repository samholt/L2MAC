import pytest
from admin import Admin
from url_shortener import URLShortener
from user import User


def test_admin():
	url_shortener = URLShortener()
	admin = Admin(url_shortener)
	user = User('test_user', 'password')
	user.create_account(url_shortener)
	short_url = user.add_url('https://www.google.com', url_shortener)

	assert len(admin.view_all_urls()) == 1
	assert admin.monitor_system() == {'users': 1, 'urls': 1, 'clicks': 0}

	admin.delete_url(short_url)
	assert len(admin.view_all_urls()) == 0

	admin.delete_user('test_user')
	assert admin.monitor_system() == {'users': 0, 'urls': 0, 'clicks': 0}
