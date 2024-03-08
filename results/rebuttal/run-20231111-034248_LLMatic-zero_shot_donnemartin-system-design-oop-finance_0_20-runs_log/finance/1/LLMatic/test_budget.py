import pytest
from budget import Budget


def test_set_budget():
	budget = Budget()
	budget.set_budget('user1', 'groceries', 200)
	assert budget.get_budget_status('user1') == {'groceries': {'limit': 200, 'current_spending': 0}}


def test_update_spending():
	budget = Budget()
	budget.set_budget('user1', 'groceries', 200)
	budget.update_spending('user1', 'groceries', 50)
	assert budget.get_budget_status('user1') == {'groceries': {'limit': 200, 'current_spending': 50}}

