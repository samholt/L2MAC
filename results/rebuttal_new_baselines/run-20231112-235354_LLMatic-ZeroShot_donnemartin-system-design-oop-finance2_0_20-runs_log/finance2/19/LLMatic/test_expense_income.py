import pytest
from expense_income import Expense, Income

def test_expense():
	expense = Expense(100, 'Groceries')
	assert expense.import_expenses([{'amount': 50, 'category': 'Groceries'}]) == [{'amount': 50, 'category': 'Groceries'}]
	assert expense.get_summary() == {'amount': 100, 'category': 'Groceries'}

def test_income():
	income = Income(1000, 'Salary')
	assert income.import_incomes([{'amount': 500, 'source': 'Part-time job'}]) == [{'amount': 500, 'source': 'Part-time job'}]
	assert income.get_summary() == {'amount': 1000, 'source': 'Salary'}
