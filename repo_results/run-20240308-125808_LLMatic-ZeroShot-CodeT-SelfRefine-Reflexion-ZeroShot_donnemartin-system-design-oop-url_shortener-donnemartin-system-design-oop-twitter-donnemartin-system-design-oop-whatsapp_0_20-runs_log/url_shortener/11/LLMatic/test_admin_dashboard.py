import admin_dashboard
import url_shortener
import analytics


USER_ACCOUNTS = admin_dashboard.USER_ACCOUNTS


def test_view_all_urls():
	url_shortener.generate_short_url('https://example.com')
	assert len(admin_dashboard.view_all_urls()) == 1


def test_delete_url():
	url = 'https://example.com'
	short_url = url_shortener.generate_short_url(url)
	assert admin_dashboard.delete_url(url) == 'URL deleted successfully.'
	assert short_url not in admin_dashboard.view_all_urls().values()


def test_delete_user():
	username = 'testuser'
	password = 'testpassword'
	USER_ACCOUNTS.create_account(username, password)
	assert admin_dashboard.delete_user(username) == 'User account deleted successfully.'
	assert username not in USER_ACCOUNTS.users


def test_monitor_system():
	short_url = url_shortener.generate_short_url('https://example.com')
	analytics.track_click(short_url, 'USA')
	assert len(admin_dashboard.monitor_system()[short_url]) == 1



