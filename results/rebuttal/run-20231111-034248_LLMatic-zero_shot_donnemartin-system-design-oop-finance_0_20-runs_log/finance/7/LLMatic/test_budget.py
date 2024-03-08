import pytest
from budget import Budget

def test_budget_system():
	budget = Budget()
	user_id = 'user1'
	category = 'groceries'
	amount = 100

	# Test setting budget
	budget.set_budget(user_id, category, amount)
	assert budget.get_budget(user_id, category) == {'budget': amount, 'progress': 0}

	# Test updating progress
	assert budget.update_progress(user_id, category, 50) == 'Budget update successful'
	assert budget.get_budget(user_id, category) == {'budget': amount, 'progress': 50}

	# Test nearing budget limit
	assert budget.update_progress(user_id, category, 40) == 'Budget limit nearing'
	assert budget.get_budget(user_id, category) == {'budget': amount, 'progress': 90}

	# Test exceeding budget limit
	assert budget.update_progress(user_id, category, 20) == 'Budget limit exceeded'
	assert budget.get_budget(user_id, category) == {'budget': amount, 'progress': 110}
