import pytest
from budget import Budget

def test_set_and_adjust_budget():
	budget = Budget()
	budget.set_budget('user1', 5000)
	assert budget.get_budget('user1') == 5000
	budget.adjust_budget('user1', 500)
	assert budget.get_budget('user1') == 5500

	budget.set_budget('user2', 3000)
	assert budget.get_budget('user2') == 3000
	budget.adjust_budget('user2', -500)
	assert budget.get_budget('user2') == 2500
