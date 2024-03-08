import pytest
from recommendation import Recommendation


def test_savings_tips():
	recommendation = Recommendation()
	recommendation.add_savings_tip('user1', 'Save money by cooking at home')
	assert recommendation.get_savings_tips('user1') == ['Save money by cooking at home']


def test_product_recommendations():
	recommendation = Recommendation()
	recommendation.add_product_recommendation('user1', 'Invest in stocks')
	assert recommendation.get_product_recommendations('user1') == ['Invest in stocks']
