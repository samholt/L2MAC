import pytest
from trending_discovery import Trending, Discovery
from user_management import User
from posting_content_management import Post


def test_trending_topics():
	trending = Trending()
	user = User('test@test.com', 'testuser', 'password')
	user.register()
	for i in range(10):
		user.post(f'Test post {i} #test')
	for post in user.posts:
		trending.add_post(Post(user.username, post))
	assert trending.get_trending_topics() == [('Test', 10), ('post', 10), ('#test', 10), ('0', 1), ('1', 1), ('2', 1), ('3', 1), ('4', 1), ('5', 1), ('6', 1)]


def test_user_recommendations():
	discovery = Discovery(User.users_db)
	user1 = User('test1@test.com', 'testuser1', 'password')
	user2 = User('test2@test.com', 'testuser2', 'password')
	user3 = User('test3@test.com', 'testuser3', 'password')
	user1.register()
	user2.register()
	user3.register()
	user1.follow('testuser2')
	user2.follow('testuser3')
	assert discovery.recommend_users('testuser1') == ['testuser3']
