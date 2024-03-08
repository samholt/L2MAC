import pytest
from budget import Budget


def test_set_monthly_budget():
	budget = Budget()
	budget.set_monthly_budget('user1', 1000)
	assert budget.get_budget_status('user1') == {'monthly_budget': 1000, 'spent': 0}


def test_add_expense():
	budget = Budget()
	budget.set_monthly_budget('user1', 1000)
	assert budget.add_expense('user1', 900) == 'Budget limit nearing'
	assert budget.add_expense('user1', 100) == 'Budget limit exceeded'


def test_get_budget_status():
	budget = Budget()
	budget.set_monthly_budget('user1', 1000)
	budget.add_expense('user1', 500)
	assert budget.get_budget_status('user1') == {'monthly_budget': 1000, 'spent': 500}
