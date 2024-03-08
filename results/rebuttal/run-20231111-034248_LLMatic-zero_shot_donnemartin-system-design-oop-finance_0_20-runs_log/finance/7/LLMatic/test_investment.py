import pytest
from investment import Investment

def test_investment():
	investment = Investment()
	investment.add_investment('Bitcoin', 1000, 50000)
	assert investment.track_investment('Bitcoin') == {'amount': 1000, 'current_value': 50000}
	assert investment.overview() == {'Bitcoin': {'amount': 1000, 'current_value': 50000}}
	assert investment.set_alert('Bitcoin', 60000) == 'Alert! The current value of Bitcoin is below the threshold'
	assert investment.set_alert('Bitcoin', 50000) == 'Alert! The current value of Bitcoin is below the threshold'
	assert investment.set_alert('Ethereum', 40000) == 'Investment not found'
