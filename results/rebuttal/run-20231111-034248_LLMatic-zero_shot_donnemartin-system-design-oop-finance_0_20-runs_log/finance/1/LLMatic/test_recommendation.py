import pytest
from recommendation import Recommendation

def test_generate_savings_tips():
	recommendation = Recommendation()
	spending_data = {'groceries': 200, 'utilities': 150, 'entertainment': 100}
	assert recommendation.generate_savings_tips('user1', spending_data) == 'Save more on entertainment'

def test_recommend_financial_products():
	recommendation = Recommendation()
	financial_profile = {'stocks': 1000, 'bonds': 500, 'real estate': 2000}
	assert recommendation.recommend_financial_products('user1', financial_profile) == 'Invest in real estate'
