import pytest
from trending import Trending

def test_trending_topics():
	trending = Trending()
	trending.add_topic('#python')
	trending.add_topic('#python')
	trending.add_topic('#ai')
	assert trending.get_trending_topics() == [('#python', 2), ('#ai', 1)]

def test_user_recommendations():
	trending = Trending()
	trending.add_user_recommendation('user1')
	trending.add_user_recommendation('user1')
	trending.add_user_recommendation('user2')
	assert trending.get_user_recommendations() == [('user1', 2), ('user2', 1)]
