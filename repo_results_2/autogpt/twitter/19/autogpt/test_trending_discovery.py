import pytest
from user_management import User
from trending_discovery import TrendingDiscovery

def test_trending_discovery():
    user = User()
    user.register('testuser', 'testpassword', 'testuser@example.com')
    trending_discovery = TrendingDiscovery()
    trending_discovery.identify_trending_topics()
    assert trending_discovery.trending_topics
    trending_discovery.display_trending_topics()
    assert trending_discovery.trending_topics
    trending_discovery.recommend_users()
    assert trending_discovery.recommended_users