import admin_dashboard as ad
import url_shortener as us
import user_accounts as ua

user_accounts = ua.UserAccounts()


def test_get_all_urls():
	us.generate_short_url('https://example.com')
	assert len(ad.get_all_urls()) >= 1


def test_delete_url():
	short_url = us.generate_short_url('https://example.com')
	assert ad.delete_url(short_url) == 'URL deleted successfully.'
	assert ad.delete_url(short_url) == 'URL does not exist.'


def test_delete_user():
	assert ad.delete_user('testuser') == 'User deleted successfully.'
	assert ad.delete_user('testuser') == 'Username does not exist.'


def test_get_system_performance():
	short_url = us.generate_short_url('https://example.com')
	assert len(ad.get_system_performance()[short_url]) == 0

