import admin

def test_admin():
	admin1 = admin.Admin(1, 'Admin1')
	admin.admins[1] = admin1

	assert admin1.monitor_activities() == 'Monitoring activities'
	assert admin1.manage_activities() == 'Managing activities'
	assert admin1.view_analytics() == 'Viewing analytics'
	assert admin1.view_statistics() == 'Viewing statistics'
	assert admin1.manage_listings() == 'Managing listings'
	assert admin1.manage_content() == 'Managing content'

