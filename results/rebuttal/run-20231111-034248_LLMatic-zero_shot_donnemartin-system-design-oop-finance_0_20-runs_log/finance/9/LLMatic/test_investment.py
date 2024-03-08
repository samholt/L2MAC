import pytest
from investment import Alert, Investment, InvestmentManager


def test_investment():
	investment = Investment('Gold', 10, 100, 120)
	assert investment.name == 'Gold'
	assert investment.quantity == 10
	assert investment.purchase_price == 100
	assert investment.current_price == 120
	assert investment.track_performance() == 200

	alert = Alert('Price Drop', 90)
	investment.add_alert(alert)
	assert investment.alerts[0].name == 'Price Drop'
	assert investment.alerts[0].threshold == 90


def test_investment_manager():
	manager = InvestmentManager()
	investment = manager.add_investment('Gold', 10, 100, 120)
	assert investment.name == 'Gold'
	assert manager.track_investment('Gold') == 200

	alert = Alert('Price Drop', 90)
	manager.set_alert('Gold', alert)
	assert manager.investments['Gold'].alerts[0].name == 'Price Drop'
	assert manager.investments['Gold'].alerts[0].threshold == 90
