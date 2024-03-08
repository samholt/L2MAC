import os

def test_file_existence():
	assert os.path.exists('app.py')
	assert os.path.exists('account.py')
	assert os.path.exists('expense_income.py')
	assert os.path.exists('budget.py')
	assert os.path.exists('investment.py')
	assert os.path.exists('reports.py')
	assert os.path.exists('database.py')
	assert os.path.exists('requirements.txt')
