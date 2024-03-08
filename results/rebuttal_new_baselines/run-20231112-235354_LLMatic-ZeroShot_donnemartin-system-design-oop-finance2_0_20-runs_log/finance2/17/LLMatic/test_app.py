import app
import pytest

def test_app():
	# Test that the user's balance is correct
	assert app.user_account.get_balance() == 5000

	# Test that the user's expenses are correct
	assert app.user_expense.visualize_expenses() == {'Rent': 1000}

	# Test that the user's incomes are correct
	assert app.user_income.visualize_incomes() == {'Salary': 5000}

	# Test that the user's budget is correct
	assert app.user_budget.get_budget('Rent') == 1200

	# Test that the user's investment balance is correct
	assert app.user_investment.balance == 5000

	# Test that the user's financial report is correct
	assert app.financial_report == {'balance': 5000, 'expenses': {'Rent': 1000}, 'income': {'Salary': 5000}}

	# Test that the data in the mock database is correct
	assert app.mock_db.get('users', 'John Doe') == {'balance': 5000, 'assets': {'Bank Account': 5000}}
	assert app.mock_db.get('expenses', 'John Doe') == {'Rent': 1000}
	assert app.mock_db.get('incomes', 'John Doe') == {'Salary': 5000}
	assert app.mock_db.get('budgets', 'John Doe') == {'Rent': 1200}
	assert app.mock_db.get('investments', 'John Doe') == {'balance': 5000, 'performance': {'John Doe': 5000}}
	assert app.mock_db.get('reports', 'John Doe') == {'balance': 5000, 'expenses': {'Rent': 1000}, 'income': {'Salary': 5000}}
