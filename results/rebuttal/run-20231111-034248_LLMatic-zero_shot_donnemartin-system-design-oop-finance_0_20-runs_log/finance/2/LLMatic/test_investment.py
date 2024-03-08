import pytest
from investment import Investment

def test_investment():
	investment = Investment()
	investment.add_investment('user1', 'investment1', 1000)
	assert investment.get_investment('user1', 'investment1') == 1000
	assert investment.get_total_investment('user1') == 1000
	investment.add_investment('user1', 'investment2', 2000)
	assert investment.get_investment('user1', 'investment2') == 2000
	assert investment.get_total_investment('user1') == 3000
	investment.set_alert('user1', 'investment1', 900)
	assert investment.get_investment('user1', 'investment1') == {'alert': 900}
	investment.set_alert('user2', 'investment1', 900)
	assert investment.set_alert('user2', 'investment1', 900) == 'User does not have any investments'
	investment.set_alert('user1', 'investment3', 900)
	assert investment.set_alert('user1', 'investment3', 900) == 'Investment not found'
