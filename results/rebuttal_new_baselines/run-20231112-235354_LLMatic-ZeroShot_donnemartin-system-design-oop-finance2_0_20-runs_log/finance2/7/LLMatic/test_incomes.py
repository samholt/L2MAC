from incomes import Income

def test_income_creation():
	income = Income(1, 2000, 'Salary', '2022-01-01')
	assert income.id == 1
	assert income.amount == 2000
	assert income.source == 'Salary'
	assert income.date == '2022-01-01'

def test_income_update():
	income = Income(1, 2000, 'Salary', '2022-01-01')
	income.update(amount=3000, source='Rent')
	assert income.amount == 3000
	assert income.source == 'Rent'

def test_income_delete():
	income = Income(1, 2000, 'Salary', '2022-01-01')
	income.delete()
	try:
		print(income)
	except NameError:
		assert True
