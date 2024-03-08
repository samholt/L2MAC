import pytest
from savings import Savings


def test_get_savings_tips():
	user = {'name': 'Test User', 'income': 5000}
	savings = Savings(user)
	assert savings.get_savings_tips() == 'Save 10% of your income each month.'


def test_get_product_recommendations():
	user = {'name': 'Test User', 'income': 5000}
	savings = Savings(user)
	assert savings.get_product_recommendations() == 'Consider investing in a low-cost index fund.'
