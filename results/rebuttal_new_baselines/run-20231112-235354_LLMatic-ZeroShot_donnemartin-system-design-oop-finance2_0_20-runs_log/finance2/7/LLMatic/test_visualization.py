import pytest
from unittest.mock import Mock
from visualization import visualize_expense_income_history


def test_visualize_expense_income_history():
	# Mock Expense and Income objects
	mock_expense = Mock()
	mock_expense.amount = 100
	mock_income = Mock()
	mock_income.amount = 200

	# Call visualize_expense_income_history function
	try:
		visualize_expense_income_history([mock_expense], [mock_income])
	except Exception as e:
		pytest.fail(f'Unexpected error occurred: {str(e)}')
