import pytest
from investment import Investment

def test_investment():
	investment = Investment(1000, 0.05, [])
	assert investment.value == 1000
	assert investment.roi == 0.05
	assert investment.alerts == []

	investment.add_investment(500)
	assert investment.value == 1500

	assert investment.calculate_roi() == 75

	investment.set_alert('ROI reached')
	assert investment.alerts == ['ROI reached']
