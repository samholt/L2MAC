import pytest
from dashboard import Dashboard
from admin import Admin
from user import User
from main import users as site


def test_dashboard():
	admin = Admin('Admin', 'admin@example.com')
	dashboard = Dashboard(admin)
	user = User('User', 'password')

	assert dashboard.monitor_user_engagement(user) == {'User': 0}
	assert dashboard.monitor_site_usage(site) == {'Site': 0}

	user.submitted_recipes.append('1')
	assert dashboard.monitor_user_engagement(user) == {'User': 1}

	site['User'] = user
	assert dashboard.monitor_site_usage(site) == {'Site': 1}
