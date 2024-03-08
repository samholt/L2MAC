import budget_management

def test_budget_management():
	budget = budget_management.Budget(1000, {'food': 500, 'decor': 500}, [])
	assert budget.track_budget() == 1000
	budget.set_budget(900)
	assert budget.track_budget() == 900
	assert budget.alert_overrun() == 'Budget is under control'
	budget.set_budget(-100)
	assert budget.alert_overrun() == 'Budget Overrun'

