import admin_dashboard


def test_view_all_urls():
	admin_dashboard.url_db = {'http://example.com': 'abc123'}
	assert admin_dashboard.view_all_urls() == {'http://example.com': 'abc123'}


def test_monitor_system():
	admin_dashboard.url_db = {'http://example.com': 'abc123'}
	admin_dashboard.user_db = {'testuser': {'password': 'password', 'urls': []}}
	assert admin_dashboard.monitor_system() == {'total_urls': 1, 'total_users': 1}
