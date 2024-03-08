import pytest
from investment import Investment

def test_add_investment():
	investment = Investment()
	investment.add_investment('Bitcoin', 10000, 15000)
	assert investment.get_investment_overview() == {'Bitcoin': {'amount_invested': 10000, 'current_value': 15000}}

def test_alert_significant_change():
	investment = Investment()
	investment.add_investment('Bitcoin', 10000, 15000)
	assert investment.alert_significant_change('Bitcoin', 20000) == 'Significant change in Bitcoin investment: 33.33%'
	assert investment.alert_significant_change('Bitcoin', 14000) == 'No significant change'
	assert investment.alert_significant_change('Ethereum', 20000) == 'Investment not found'
