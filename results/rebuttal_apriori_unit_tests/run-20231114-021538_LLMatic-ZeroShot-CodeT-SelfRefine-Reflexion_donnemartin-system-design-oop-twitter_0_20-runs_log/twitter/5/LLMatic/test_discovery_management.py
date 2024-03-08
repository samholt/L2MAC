import pytest
from discovery_management import get_trending_topics, get_user_recommendations


def test_trending_topics():
	topics = get_trending_topics()
	assert isinstance(topics, list)
	assert len(topics) == 10


def test_user_recommendations():
	recommendations = get_user_recommendations(1)
	assert isinstance(recommendations, list)
	assert len(recommendations) == 10

