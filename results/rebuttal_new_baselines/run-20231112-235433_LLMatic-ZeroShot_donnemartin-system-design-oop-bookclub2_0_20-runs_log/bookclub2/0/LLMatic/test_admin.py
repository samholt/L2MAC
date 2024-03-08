from admin import Admin

def test_admin():
	admin = Admin('user1', 'dashboard1')
	assert admin.moderate_content('content1') == 'Content moderated'
	assert admin.manage_users('user2') == 'User managed'
	assert admin.view_analytics() == 'Analytics viewed'
