import pytest
from investments import Investment

def test_investment():
	investment = Investment()

	# Test adding portfolio
	assert investment.add_portfolio('Tech', 1000) == 'Portfolio added successfully.'
	assert investment.add_portfolio('Tech', 1000) == 'Portfolio already exists.'

	# Test tracking portfolio
	assert investment.track_portfolio('Tech', 1200) == 'Portfolio updated successfully.'
	assert investment.track_portfolio('Nonexistent', 1200) == 'Portfolio does not exist.'

	# Test overview
	assert investment.overview() == {'Tech': {'investment': 1000, 'value': 1200}}

	# Test setting alert
	assert investment.set_alert('Tech', 900) == 'Alert set successfully.'
	assert investment.set_alert('Nonexistent', 900) == 'Portfolio does not exist.'

	# Test checking alerts
	assert investment.check_alerts() == []
	assert investment.track_portfolio('Tech', 800) == 'Portfolio updated successfully.'
	assert investment.check_alerts() == ['Tech has reached the alert threshold.']
