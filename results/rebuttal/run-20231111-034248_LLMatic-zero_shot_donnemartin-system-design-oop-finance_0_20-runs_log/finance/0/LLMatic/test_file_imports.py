import os


def test_file_imports():
	assert os.path.exists('app.py')
	assert os.path.exists('user.py')
	assert os.path.exists('transaction.py')
	assert os.path.exists('budget.py')
	assert os.path.exists('investment.py')
	assert os.path.exists('analytics.py')
	assert os.path.exists('notifications.py')
	assert os.path.exists('support.py')
	assert os.path.exists('requirements.txt')
