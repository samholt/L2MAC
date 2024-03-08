import pytest
from recommendation import Recommendation


def test_set_user_preferences():
	recommendation = Recommendation()
	recommendation.set_user_preferences('user1', ['Italian', 'Mexican'])
	assert recommendation.user_preferences['user1'] == ['Italian', 'Mexican']


def test_track_user_activity():
	recommendation = Recommendation()
	recommendation.track_user_activity('user1', 'viewed recipe1')
	assert recommendation.user_activity['user1'] == ['viewed recipe1']


def test_generate_recommendations():
	recommendation = Recommendation()
	recommendation.set_user_preferences('user1', ['Italian', 'Mexican'])
	recommendations = recommendation.generate_recommendations('user1')
	assert isinstance(recommendations, list)


def test_notify_user():
	recommendation = Recommendation()
	recommendation.notify_user('user1', ['recipe1', 'recipe2'])
	assert recommendation.notifications['user1'] == ['recipe1', 'recipe2']
