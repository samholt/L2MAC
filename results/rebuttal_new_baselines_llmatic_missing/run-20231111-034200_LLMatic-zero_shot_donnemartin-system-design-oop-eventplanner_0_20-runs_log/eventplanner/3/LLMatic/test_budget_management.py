import pytest
import budget_management


def test_set_get_budget():
	budget = budget_management.Budget(1000, {'food': 500, 'decor': 500})
	assert budget.get_budget() == (1000, {'food': 500, 'decor': 500})

	budget.set_budget(2000, {'food': 1000, 'decor': 1000})
	assert budget.get_budget() == (2000, {'food': 1000, 'decor': 1000})


def test_update_budget():
	budget = budget_management.Budget(1000, {'food': 500, 'decor': 500})
	budget.update_budget('food', 600)
	assert budget.get_budget() == (1000, {'food': 1100, 'decor': 500})
	assert 'Over budget in food!' in budget.get_alerts()

	budget.update_budget('entertainment', 100)
	assert 'Category entertainment does not exist.' in budget.get_alerts()

