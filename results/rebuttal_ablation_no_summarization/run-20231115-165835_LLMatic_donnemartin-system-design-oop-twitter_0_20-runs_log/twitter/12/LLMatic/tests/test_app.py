import pytest
import app
import user
import post


def test_get_trending_topics():
	app.Post.posts_db = {
		'user1': [app.Post('user1', '#trending #topic'), app.Post('user1', '#topic')],
		'user2': [app.Post('user2', '#trending')]
	}
	trending_topics = app.get_trending_topics()
	assert trending_topics == [('trending', 2), ('topic', 2)]


def test_recommend_users():
	app.User.users_db = {
		'user1': app.User('user1', 'email1', 'password1'),
		'user2': app.User('user2', 'email2', 'password2'),
		'user3': app.User('user3', 'email3', 'password3'),
		'user4': app.User('user4', 'email4', 'password4'),
		'user5': app.User('user5', 'email5', 'password5'),
		'user6': app.User('user6', 'email6', 'password6')
	}
	app.User.users_db['user1'].following = ['user2', 'user3']
	recommended_users = app.recommend_users_to_follow('user1')
	assert len(recommended_users) == 3
	assert 'user1' not in recommended_users
	assert 'user2' not in recommended_users
	assert 'user3' not in recommended_users
