import pytest
from trending import get_trending_hashtags, recommend_users
from models import User, Post, users_db, posts_db


def setup_module(module):
	users_db.clear()
	posts_db.clear()
	for i in range(1, 11):
		user = User(i, f'user{i}', f'user{i}@oms.com', 'password')
		users_db[i] = user
		for j in range(1, 11):
			post = Post((i-1)*10+j, i, f'#hashtag{j} Post{j}')
			posts_db[post.id] = post


def test_get_trending_hashtags():
	trending_hashtags = get_trending_hashtags()
	assert len(trending_hashtags) == 10
	assert all(hashtag[1] == 10 for hashtag in trending_hashtags)


def test_recommend_users():
	for i in range(1, 11):
		recommended_users = recommend_users(i)
		assert len(recommended_users) == 9
		assert all(user.id != i for user in recommended_users)
