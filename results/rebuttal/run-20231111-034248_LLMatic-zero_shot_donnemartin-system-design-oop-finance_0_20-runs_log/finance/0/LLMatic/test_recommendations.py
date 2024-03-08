import pytest
from recommendations import Recommendations


def test_recommendations():
	recommendations = Recommendations()
	assert recommendations.add_recommendation('user1', 'Invest in stocks') == 'Recommendation added successfully'
	assert recommendations.get_recommendations('user1') == ['Invest in stocks']
	assert recommendations.get_recommendations('user2') == 'No recommendations available'

