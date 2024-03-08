import pytest
import budget_management

def test_budget_management():
	budget = budget_management.Budget(1000, {'food': 500, 'decorations': 500})
	budget_management.mock_database['test_event'] = budget

	budget_management.mock_database['test_event'].set_budget(2000, {'food': 1000, 'decorations': 1000})
	assert budget_management.mock_database['test_event'].total_budget == 2000
	assert budget_management.mock_database['test_event'].breakdown == {'food': 1000, 'decorations': 1000}

	budget_management.mock_database['test_event'].track_budget('food', 1100)
	assert budget_management.mock_database['test_event'].breakdown == {'food': -100, 'decorations': 1000}
	assert budget_management.mock_database['test_event'].get_alerts() == ['Over budget in food by 100']

