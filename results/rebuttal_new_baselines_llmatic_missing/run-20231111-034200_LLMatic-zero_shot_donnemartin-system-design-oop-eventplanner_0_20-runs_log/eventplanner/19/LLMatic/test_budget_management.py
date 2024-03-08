import pytest
from budget_management import BudgetManagement

def test_budget_management():
	bm = BudgetManagement()
	bm.set_budget('event1', 1000)
	bm.add_category('event1', 'food', 500)
	bm.track_spending('event1', 'food', 200)
	assert bm.check_budget('event1') == 'Budget is under control'
	bm.track_spending('event1', 'food', 800)
	assert bm.check_budget('event1') == 'Budget overrun'
	breakdown = bm.breakdown('event1')
	assert breakdown['total_budget'] == 1000
	assert breakdown['spent'] == 1000
	assert breakdown['categories']['food']['budget'] == 500
	assert breakdown['categories']['food']['spent'] == 1000
