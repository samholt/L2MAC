import pytest
from budget import Budget


def test_budget_system():
	budget = Budget()
	user_id = 'user1'
	category = 'groceries'
	amount = 500

	# Test setting a monthly budget
	budget.set_monthly_budget(user_id, category, amount)
	assert budget.get_budget_status(user_id, category) == {'budget': amount, 'spent': 0}

	# Test adding an expense
	budget.add_expense(user_id, category, 100)
	assert budget.get_budget_status(user_id, category) == {'budget': amount, 'spent': 100}

	# Test nearing budget limit
	assert budget.add_expense(user_id, category, 350) == 'You are nearing your budget limit.'
	assert budget.get_budget_status(user_id, category) == {'budget': amount, 'spent': 450}

	# Test exceeding budget limit
	assert budget.add_expense(user_id, category, 100) == 'Budget limit exceeded!'
	assert budget.get_budget_status(user_id, category) == {'budget': amount, 'spent': 550}
