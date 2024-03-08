from recommendation import Recommendation

def test_generate_recommendations():
	recommendation = Recommendation('User 1')
	assert recommendation.generate_recommendations() == ['Recipe 1', 'Recipe 2', 'Recipe 3']
