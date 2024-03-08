import pytest
import admin_dashboard
import database


def test_admin_dashboard():
	admin = admin_dashboard.Admin('1', 'Admin1')
	database.save_to_db('admins', '1', admin)
	admin.monitor_user_activities('user1', 'login')
	admin.monitor_system_performance({'CPU': '70%', 'RAM': '60%'})
	admin.manage_platform_content({'events': 'Event1'})
	assert admin_dashboard.view_dashboard(admin) == {'user_activities': {'user1': 'login'}, 'system_performance': {'CPU': '70%', 'RAM': '60%'}, 'platform_content': {'events': 'Event1'}}
