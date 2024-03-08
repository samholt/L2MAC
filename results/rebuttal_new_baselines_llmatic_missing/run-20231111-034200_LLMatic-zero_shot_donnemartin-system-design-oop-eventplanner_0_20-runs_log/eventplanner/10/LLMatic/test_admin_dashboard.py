import pytest
from admin_dashboard import Admin
from database import Database

def test_admin_dashboard():
	admin = Admin('Admin', 'admin@example.com')
	user_id = 'user1'
	activity = 'activity1'
	vendor_id = 'vendor1'
	listing = 'listing1'
	content_id = 'content1'
	content = 'content1'

	admin.manage_user_activities(user_id, activity)
	assert admin.monitor_user_activities(user_id) == activity

	assert admin.view_system_performance() == 'System Performance'
	assert admin.view_user_engagement() == 'User Engagement'

	admin.manage_vendor_listings(vendor_id, listing)
	assert admin.db.get(vendor_id) == listing

	admin.manage_platform_content(content_id, content)
	assert admin.db.get(content_id) == content
