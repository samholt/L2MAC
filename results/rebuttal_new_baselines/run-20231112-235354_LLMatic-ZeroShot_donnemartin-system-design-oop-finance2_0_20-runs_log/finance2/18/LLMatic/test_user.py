import pytest
from user import User
from finance import Expense, Income

def test_user():
	user = User('testuser', 'testpassword')
	assert user.username == 'testuser'
	assert user.password == 'testpassword'

	expense = Expense(100, 'Groceries', '2022-01-01')
	user.add_expense(expense)
	assert user.expenses[0] == expense

	income = Income(1000, 'Salary', '2022-01-01')
	user.add_income(income)
	assert user.incomes[0] == income
