import pytest
from investment import Investment

def test_investment_system():
	investment = Investment()

	# Test adding an investment
	investment.add_investment('user1', 'Investment1', 1000, 10)
	assert investment.get_investment_overview('user1') == [{'investment_name': 'Investment1', 'current_value': 1000, 'return_on_investment': 10}]

	# Test setting an investment alert
	investment.set_investment_alert('user1', 'Investment1', 900)
	assert investment.get_investment_overview('user1') == [{'investment_name': 'Investment1', 'current_value': 1000, 'return_on_investment': 10, 'alert_value': 900}]

	# Test investment not found
	assert investment.set_investment_alert('user1', 'Investment2', 900) == 'Investment not found'
