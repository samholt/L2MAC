import pytest
from budget_management import Budget

def test_budget_management():
	budget = Budget(1000)
	budget.set_category_budget('Food', 500)
	budget.track_spending('Food', 600)
	assert budget.alert_overrun() == 'Alert: You have exceeded your budget for Food!'

	budget.track_spending('Food', -100)
	assert budget.alert_overrun() == 'No budget overrun.'
