import admin_dashboard as ad
import url_shortener as us
import user_accounts as ua


def test_view_all_urls():
	us.generate_short_url('https://example.com')
	assert len(ad.view_all_urls()) == 1


def test_delete_url():
	short_url = us.generate_short_url('https://example.com')
	assert ad.delete_url(short_url) == 'URL deleted successfully.'
	assert ad.delete_url(short_url) == 'URL does not exist.'


def test_delete_user_account():
	ua.USER_ACCOUNTS.create_account('test', 'password')
	assert ad.delete_user_account('test') == 'User account deleted successfully.'
	assert ad.delete_user_account('test') == 'User account does not exist.'


def test_view_system_performance():
	assert isinstance(ad.view_system_performance(), dict)

