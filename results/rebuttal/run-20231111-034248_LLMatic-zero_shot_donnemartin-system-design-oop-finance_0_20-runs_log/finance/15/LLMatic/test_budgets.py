import pytest
from budgets import Budget

def test_set_get_budget():
	budget = Budget()
	budget.set_budget('Groceries', 200)
	assert budget.get_budget('Groceries') == 200


def test_check_budget():
	budget = Budget()
	budget.set_budget('Groceries', 200)
	assert budget.check_budget('Groceries', 180) == 'Nearing'
	assert budget.check_budget('Groceries', 210) == 'Exceeded'
	assert budget.check_budget('Groceries', 150) == 'Safe'


def test_track_progress():
	budget = Budget()
	budget.set_budget('Groceries', 200)
	assert budget.track_progress('Groceries', 100) == 50
