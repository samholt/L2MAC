import pytest
from recommendation import Recommendation, RecommendationManager
from user import User


def test_recommendation():
	user = User('John Doe', 'password', 'john.doe@example.com')
	recommendation = Recommendation(user)
	recommendation.generate_tips()
	recommendation.recommend_products()
	assert len(recommendation.tips) == 1
	assert recommendation.tips[0] == 'Save more money'
	assert recommendation.financial_products == ['Investment product']


def test_recommendation_manager():
	manager = RecommendationManager()
	user = User('John Doe', 'password', 'john.doe@example.com')
	recommendation = manager.create_recommendation(user)
	assert recommendation == manager.get_recommendation(user.username)
	assert recommendation.tips == ['Save more money']
	assert recommendation.financial_products == ['Investment product']
