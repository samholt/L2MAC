import os


def test_file_imports():
	files = ['app.py', 'user.py', 'transaction.py', 'budget.py', 'investment.py', 'analytics.py', 'notification.py', 'support.py', 'requirements.txt']
	for file in files:
		assert os.path.exists(file), f'{file} does not exist.'
