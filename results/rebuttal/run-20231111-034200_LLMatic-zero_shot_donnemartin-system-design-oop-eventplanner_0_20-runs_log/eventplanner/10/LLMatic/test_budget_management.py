import pytest
from budget_management import BudgetManagement


def test_set_and_track_budget():
	bm = BudgetManagement()
	bm.set_budget('event1', 1000, {'food': 500, 'decorations': 500})
	assert bm.track_budget('event1', 200) == 'Budget updated'
	assert bm.track_budget('event1', 900) == 'Budget overrun'
	assert bm.track_budget('event2', 200) == 'Budget not found'

