import admin
import database

def test_admin_and_database():
	db = database.Database()
	admin1 = admin.Admin('admin1', 'Admin One')
	db.add_admin('admin1', admin1)
	assert db.get_admin('admin1') == admin1

	admin1.monitor_user_activities('user1', 'Logged in')
	assert admin1.user_activities['user1'] == 'Logged in'

	admin1.manage_platform_content('content1', 'New Content')
	assert admin1.get_platform_content('content1') == 'New Content'
