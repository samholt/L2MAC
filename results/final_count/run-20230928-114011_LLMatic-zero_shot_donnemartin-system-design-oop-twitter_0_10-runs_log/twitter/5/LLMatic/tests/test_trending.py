import pytest
from trending import TrendingTopic
from post import Post
from user import User


def test_add_post():
	trending = TrendingTopic('Python')
	post = Post('user1', 'I love Python', ['image1'])
	trending.add_post(post)
	assert post in trending.related_posts


def test_display_trending():
	trending = TrendingTopic('Python')
	post1 = Post('user1', 'I love Python', ['image1'])
	post1.likes = 10
	post2 = Post('user2', 'Python is great', ['image2'])
	post2.retweets = 20
	trending.add_post(post1)
	trending.add_post(post2)
	assert trending.display_trending() == [post2, post1]


def test_recommend_users():
	user1 = User('user1', 'user1@example.com', 'password1')
	user1.bio = 'I love Python'
	user1.posts = ['post1', 'post2', 'post3']
	user1.followers = ['user2', 'user3']
	user2 = User('user2', 'user2@example.com', 'password2')
	user2.bio = 'I love Java'
	user2.posts = ['post1']
	user2.followers = ['user1']
	users = [user1, user2]
	interests = ['Python']
	activity = 2
	mutual_followers = 1
	assert TrendingTopic.recommend_users(users, interests, activity, mutual_followers) == [user1]
