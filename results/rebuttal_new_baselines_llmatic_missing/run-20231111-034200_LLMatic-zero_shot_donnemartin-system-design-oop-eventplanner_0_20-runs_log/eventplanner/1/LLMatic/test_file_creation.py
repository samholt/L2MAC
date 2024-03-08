import os


def test_file_creation():
	files = ['app.py', 'events.py', 'venues.py', 'guests.py', 'vendors.py', 'budget.py', 'users.py', 'notifications.py', 'reports.py', 'admin.py', 'security.py', 'database.py', 'requirements.txt']
	for file in files:
		assert os.path.exists(file), f'{file} does not exist'
