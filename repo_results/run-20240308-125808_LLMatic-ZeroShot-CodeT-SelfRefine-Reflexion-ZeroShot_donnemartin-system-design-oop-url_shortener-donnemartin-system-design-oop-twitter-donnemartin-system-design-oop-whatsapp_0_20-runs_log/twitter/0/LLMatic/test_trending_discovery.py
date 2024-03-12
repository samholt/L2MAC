import pytest
from posting_content_management import PostingContentManagement, Post
from user_management import User, UserManagement
from trending_discovery import TrendingDiscovery, TrendingTopic


def test_trending_discovery():
	user_management = UserManagement()
	user_management.register('test@test.com', 'test', 'password')
	user = user_management.login('test@test.com', 'password')

	posting_content_management = PostingContentManagement()
	posting_content_management.create_post(user, 'Hello #world!', ['#world'])
	posting_content_management.create_post(user, 'Hello #python!', ['#python'])
	posting_content_management.create_post(user, 'Hello #world!', ['#world'])

	trending_discovery = TrendingDiscovery()
	trending_discovery.identify_trending_topics(posting_content_management.posts)
	trending_topics = trending_discovery.display_trending_topics()

	assert len(trending_topics) == 2
	assert trending_topics[0].topic == '#world'
	assert trending_topics[0].count == 2
	assert trending_topics[1].topic == '#python'
	assert trending_topics[1].count == 1

	recommended_users = user.recommend_users(user_management.users)
	assert len(recommended_users) == 1
