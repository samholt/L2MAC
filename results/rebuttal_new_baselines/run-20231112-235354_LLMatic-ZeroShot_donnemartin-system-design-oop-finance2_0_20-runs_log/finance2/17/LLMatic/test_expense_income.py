import pytest
from expense_income import Expense, Income

def test_expense():
	expense = Expense()
	expense.import_expenses([{'name': 'Rent', 'amount': 1000}, {'name': 'Groceries', 'amount': 200}])
	assert expense.expenses == {'Rent': 1000, 'Groceries': 200}
	expense.categorize_expenses([{'name': 'Housing', 'amount': 1000}, {'name': 'Food', 'amount': 200}])
	assert expense.expenses == {'Housing': 1000, 'Food': 200}
	assert expense.visualize_expenses() == {'Housing': 1000, 'Food': 200}

def test_income():
	income = Income()
	income.import_incomes([{'name': 'Salary', 'amount': 3000}, {'name': 'Freelance', 'amount': 500}])
	assert income.incomes == {'Salary': 3000, 'Freelance': 500}
	income.categorize_incomes([{'name': 'Job', 'amount': 3000}, {'name': 'Side Hustle', 'amount': 500}])
	assert income.incomes == {'Job': 3000, 'Side Hustle': 500}
	assert income.visualize_incomes() == {'Job': 3000, 'Side Hustle': 500}
