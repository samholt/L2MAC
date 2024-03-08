import pytest
from budget import Budget

def test_budget():
	budget = Budget(1000)
	assert budget.monthly_budget == 1000

	budget.set_budget(2000)
	assert budget.monthly_budget == 2000

	budget.adjust_budget(500)
	assert budget.monthly_budget == 2500

	budget.generate_alert(2300)
	assert 'You are nearing your budget limit.' in budget.get_alerts()

	budget.generate_alert(2400)
	assert 'You are nearing your budget limit.' in budget.get_alerts()
