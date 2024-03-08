import pytest
import trending

def test_get_trending_hashtags():
	# Clear the mock database
	trending.posts_db = []
	# Add posts to the mock database
	trending.add_post_to_db({'text': '#test #test2 #test'})
	trending.add_post_to_db({'text': '#test #test2'})
	trending.add_post_to_db({'text': '#test'})
	# Check that the function correctly identifies the trending hashtags
	assert trending.get_trending_hashtags() == [('#test', 4), ('#test2', 2)]

def test_recommend_users():
	# Clear the mock database
	trending.users_db = {}
	# Add users to the mock database
	trending.add_user_to_db({'username': 'user1', 'following': []})
	trending.add_user_to_db({'username': 'user2', 'following': []})
	trending.add_user_to_db({'username': 'user3', 'following': []})
	trending.add_user_to_db({'username': 'user4', 'following': []})
	trending.add_user_to_db({'username': 'user5', 'following': []})
	trending.add_user_to_db({'username': 'user6', 'following': []})
	# Check that the function correctly recommends users to follow
	assert trending.recommend_users('user1') == ['user1', 'user2', 'user3', 'user4', 'user5']
