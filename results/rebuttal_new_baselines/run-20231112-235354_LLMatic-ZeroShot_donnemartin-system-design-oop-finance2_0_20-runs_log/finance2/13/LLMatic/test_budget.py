import pytest
from budget import Budget

def test_set_budget():
	budget = Budget(1000)
	budget.set_budget(2000)
	assert budget.monthly_budget == 2000

def test_adjust_budget():
	budget = Budget(1000)
	budget.adjust_budget(500)
	assert budget.monthly_budget == 1500

def test_alert_user():
	budget = Budget(1000)
	budget.current_spending = 950
	assert budget.alert_user() == 'You are nearing your budget limit.'

def test_analyze_spending():
	budget = Budget(1000)
	spending_history = [1200, 1100, 1300, 1400, 1500]
	assert budget.analyze_spending(spending_history) == 'Consider adjusting your budget.'
