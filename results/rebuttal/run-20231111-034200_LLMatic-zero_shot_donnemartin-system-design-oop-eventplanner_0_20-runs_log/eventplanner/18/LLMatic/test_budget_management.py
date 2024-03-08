import pytest
from budget_management import Budget

def test_budget_management():
	budget = Budget(1000, {'Food': 500, 'Decorations': 500})
	assert budget.track_spending('Food', 600) == 'Budget overrun in Food'
	assert budget.track_spending('Decorations', 400) == 'Spending tracked'
	assert budget.get_spent() == {'Food': 600, 'Decorations': 400}
	assert budget.get_remaining() == {'Food': -100, 'Decorations': 100}
