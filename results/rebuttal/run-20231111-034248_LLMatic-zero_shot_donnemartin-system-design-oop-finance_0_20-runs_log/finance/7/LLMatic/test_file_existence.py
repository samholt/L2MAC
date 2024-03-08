import os


def test_files_exist():
	assert os.path.exists('app.py')
	assert os.path.exists('user.py')
	assert os.path.exists('transaction.py')
	assert os.path.exists('bank_account.py')
	assert os.path.exists('budget.py')
	assert os.path.exists('investment.py')
	assert os.path.exists('analytics.py')
	assert os.path.exists('notification.py')
	assert os.path.exists('support.py')
	assert os.path.exists('requirements.txt')
