from services import get_trending_hashtags, get_recommended_users
from models import User, Post


def test_get_trending_hashtags():
	# TODO: Mock database with posts
	posts = []
	trending = get_trending_hashtags()
	assert len(trending) <= 10
	for hashtag, count in trending:
		assert hashtag.startswith('#')
		assert count == sum(post.text.count(hashtag) for post in posts)


def test_get_recommended_users():
	# TODO: Mock database with users
	users = []
	user = User(id=None, email=None, username=None, password=None, profile_picture=None, bio=None, website_link=None, location=None)
	user.following = users[:5]
	recommended = get_recommended_users(user.id)
	assert len(recommended) <= 10
	for recommended_user in recommended:
		assert recommended_user not in user.following
		assert len(set(user.following) & set(recommended_user.following)) > 0
