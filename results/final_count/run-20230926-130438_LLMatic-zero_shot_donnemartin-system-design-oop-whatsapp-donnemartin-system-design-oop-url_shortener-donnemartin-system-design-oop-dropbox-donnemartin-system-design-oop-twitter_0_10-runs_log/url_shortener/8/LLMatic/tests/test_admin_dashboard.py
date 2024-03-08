from services.admin_dashboard import AdminDashboard


def test_view_all_urls():
	admin = AdminDashboard()
	assert admin.view_all_urls() == {}


def test_delete_url():
	admin = AdminDashboard()
	admin.urls = {'test_url': 'test'}
	admin.delete_url('test_url')
	assert admin.urls == {}


def test_delete_user():
	admin = AdminDashboard()
	admin.users = {'test_user': 'test'}
	admin.delete_user('test_user')
	assert admin.users == {}


def test_monitor_system():
	admin = AdminDashboard()
	admin.users = {'test_user': 'test'}
	admin.urls = {'test_url': 'test'}
	assert admin.monitor_system() == {'users': 1, 'urls': 1}
