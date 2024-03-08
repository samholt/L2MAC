import pytest
from investment import Investment

def test_add_investment():
	investment = Investment()
	investment.add_investment('Bitcoin', 1000, 50000)
	assert investment.get_investment_overview() == {'Bitcoin': {'amount': 1000, 'current_value': 50000}}

def test_get_investment_overview():
	investment = Investment()
	investment.add_investment('Bitcoin', 1000, 50000)
	investment.add_investment('Ethereum', 500, 20000)
	assert investment.get_investment_overview() == {'Bitcoin': {'amount': 1000, 'current_value': 50000}, 'Ethereum': {'amount': 500, 'current_value': 20000}}

def test_set_alert():
	investment = Investment()
	investment.add_investment('Bitcoin', 1000, 50000)
	assert investment.set_alert('Bitcoin', 60000) == 'Alert: Your investment in Bitcoin has fallen below the threshold'
	assert investment.set_alert('Bitcoin', 40000) == 'Your investment in Bitcoin is safe'
	assert investment.set_alert('Ethereum', 20000) == 'No investment found with the name Ethereum'
