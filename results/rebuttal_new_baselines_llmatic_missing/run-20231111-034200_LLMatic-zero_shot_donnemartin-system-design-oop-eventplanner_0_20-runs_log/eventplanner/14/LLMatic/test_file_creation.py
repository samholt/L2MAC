import os


def test_file_creation():
	files = ['app.py', 'event_management.py', 'venue_sourcing.py', 'guest_list_management.py', 'vendor_coordination.py', 'budget_management.py', 'user_accounts.py', 'notifications.py', 'reporting.py', 'admin_dashboard.py', 'security.py', 'database.py', 'requirements.txt']
	for file in files:
		assert os.path.exists(file), f'{file} does not exist'
