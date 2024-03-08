import pytest
from budget import Budget


def test_set_monthly_budget():
	budget = Budget()
	budget.set_monthly_budget('user1', 'groceries', 500)
	assert budget.budget_db['user1']['groceries']['budget'] == 500


def test_get_budget_status():
	budget = Budget()
	budget.set_monthly_budget('user1', 'groceries', 500)
	assert budget.get_budget_status('user1', 'groceries') == 'You are within your budget for this category.'
	budget.update_budget_progress('user1', 'groceries', 450)
	assert budget.get_budget_status('user1', 'groceries') == 'You are nearing your budget limit for this category.'
	budget.update_budget_progress('user1', 'groceries', 100)
	assert budget.get_budget_status('user1', 'groceries') == 'You have exceeded your budget for this category.'


def test_update_budget_progress():
	budget = Budget()
	budget.set_monthly_budget('user1', 'groceries', 500)
	budget.update_budget_progress('user1', 'groceries', 100)
	assert budget.budget_db['user1']['groceries']['progress'] == 100
