import pytest
from investment import Investment

def test_investment():
	investment = Investment()
	investment.add_portfolio('Tech', 1000)
	investment.track_portfolio('Tech', 1200)
	assert investment.portfolios['Tech']['value'] == 1200
	assert investment.overview()['profit'] == 200
	investment.set_alert('Tech', 1100)
	assert investment.portfolios['Tech']['alert'] == 1100
