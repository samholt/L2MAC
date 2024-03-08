import os

def test_files_exist():
	assert os.path.exists('app.py')
	assert os.path.exists('user.py')
	assert os.path.exists('finance.py')
	assert os.path.exists('budget.py')
	assert os.path.exists('investment.py')
	assert os.path.exists('report.py')
	assert os.path.exists('requirements.txt')
