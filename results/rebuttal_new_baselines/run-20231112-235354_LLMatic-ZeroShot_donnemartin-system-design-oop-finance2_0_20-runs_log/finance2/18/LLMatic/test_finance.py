import pytest
from finance import Expense, Income

def test_expense():
	expense = Expense(100, 'Groceries', '2022-01-01')
	assert expense.amount == 100
	assert expense.category == 'Groceries'
	assert expense.date == '2022-01-01'

def test_income():
	income = Income(1000, 'Salary', '2022-01-01')
	assert income.amount == 1000
	assert income.source == 'Salary'
	assert income.date == '2022-01-01'
