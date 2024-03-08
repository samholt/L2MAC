import budget_management

def test_import():
	assert budget_management is not None

def test_set_budget():
	budget = budget_management.Budget()
	budget.set_budget(1000)
	assert budget.budget == 1000

def test_track_expense():
	budget = budget_management.Budget()
	budget.set_budget(1000)
	budget.track_expense(500)
	assert budget.expenses == 500

def test_alert_overrun():
	budget = budget_management.Budget()
	budget.set_budget(1000)
	budget.track_expense(1500)
	assert budget.expenses > budget.budget

