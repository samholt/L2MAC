from expenses import Expense

def test_expense_creation():
	expense = Expense(1, 200, 'Groceries', '2022-01-01')
	assert expense.id == 1
	assert expense.amount == 200
	assert expense.category == 'Groceries'
	assert expense.date == '2022-01-01'

def test_expense_update():
	expense = Expense(1, 200, 'Groceries', '2022-01-01')
	expense.update(amount=300, category='Rent')
	assert expense.amount == 300
	assert expense.category == 'Rent'

def test_expense_delete():
	expense = Expense(1, 200, 'Groceries', '2022-01-01')
	expense.delete()
	try:
		print(expense)
	except NameError:
		assert True
