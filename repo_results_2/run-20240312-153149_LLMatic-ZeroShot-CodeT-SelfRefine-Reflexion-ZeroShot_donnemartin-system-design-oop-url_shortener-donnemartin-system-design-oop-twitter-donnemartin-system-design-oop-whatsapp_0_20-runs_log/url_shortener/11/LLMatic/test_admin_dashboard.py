import admin_dashboard
import url_shortener
import user_accounts
import analytics

def test_view_all_urls():
	url_shortener.url_database = {'test': 'http://test.com'}
	assert admin_dashboard.view_all_urls() == {'test': 'http://test.com'}

def test_delete_url():
	url_shortener.url_database = {'test': 'http://test.com'}
	assert admin_dashboard.delete_url('test') == 'URL deleted successfully.'
	assert admin_dashboard.delete_url('test') == 'URL does not exist.'

def test_delete_user():
	admin_dashboard.user_account.accounts = {'test': {'password': 'test', 'urls': []}}
	assert admin_dashboard.delete_user('test') == 'User deleted successfully.'
	assert admin_dashboard.delete_user('test') == 'User does not exist.'

def test_monitor_system():
	url_shortener.url_database = {'test': 'http://test.com'}
	admin_dashboard.user_account.accounts = {'test': {'password': 'test', 'urls': []}}
	analytics.analytics_db = {'test': []}
	assert admin_dashboard.monitor_system() == {
		'urls': {'test': 'http://test.com'},
		'users': {'test': {'password': 'test', 'urls': []}},
		'analytics': {'test': []}
	}
