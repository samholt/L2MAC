from expense_income import Expense, Income
from datetime import datetime


def test_expense():
	expense = Expense(100, 'Groceries')
	assert expense.amount == 100
	assert expense.category == 'Groceries'
	assert isinstance(expense.date, datetime)

	expense.add_expense(200, 'Rent')
	assert expense.amount == 200
	assert expense.category == 'Rent'
	assert isinstance(expense.date, datetime)


def test_income():
	income = Income(1000, 'Salary')
	assert income.amount == 1000
	assert income.category == 'Salary'
	assert isinstance(income.date, datetime)

	income.add_income(2000, 'Bonus')
	assert income.amount == 2000
	assert income.category == 'Bonus'
	assert isinstance(income.date, datetime)
