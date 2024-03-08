from budget import Budget

def test_budget():
	budget = Budget()
	budget.set_budget(1000, {'Food': 500, 'Decorations': 500})
	assert budget.get_budget_status() == {'total_budget': 1000, 'category_budgets': {'Food': 500, 'Decorations': 500}, 'category_expenses': {'Food': 0, 'Decorations': 0}}
	assert budget.track_expense('Food', 600) == 'Budget overrun in Food'
	assert budget.track_expense('Decorations', 400) == 'Expense tracked'
	assert budget.get_budget_status() == {'total_budget': 1000, 'category_budgets': {'Food': 500, 'Decorations': 500}, 'category_expenses': {'Food': 600, 'Decorations': 400}}
