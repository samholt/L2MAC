import pytest
from investment import Investment

def test_investment():
	investment = Investment()

	investment.add_investment('Stock A', 1000)
	assert investment.investments['Stock A'] == 1000

	change = investment.track_investment('Stock A', 1100)
	assert change == 0.1

	alert = investment.alert_significant_change('Stock A', 1200)
	assert alert == 'Significant change in Stock A! Change: 20.0%'

	alert = investment.alert_significant_change('Stock A', 1050)
	assert alert == 'No significant change.'
