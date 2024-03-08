import pytest
from recommendation import Recommendation
from user import User

def test_generate_recommendations():
	user = User('test_user', 'password')
	user.set_preferences(['vegan', 'gluten-free'])
	recommendation = Recommendation(user)
	recommendations = recommendation.generate_recommendations()
	assert recommendations == ['recipe1'], 'Recommendations are not generated correctly'
