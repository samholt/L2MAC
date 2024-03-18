import pytest
from user import User
from recommendation import Recommendation

def test_get_recommendations():
	user_class = User()
	user_class.register('test1@test.com', 'test1', 'password1')
	user_class.register('test2@test.com', 'test2', 'password2')
	user_class.register('test3@test.com', 'test3', 'password3')
	user_class.register('test4@test.com', 'test4', 'password4')
	user_class.follow_user('test1', 'test2')
	user_class.follow_user('test2', 'test3')
	user_class.follow_user('test3', 'test1')
	user_class.follow_user('test3', 'test2')
	user_class.follow_user('test2', 'test4')
	recommendation_class = Recommendation(user_class)
	assert sorted(recommendation_class.get_recommendations('test1')) == sorted(['test3', 'test4'])
	assert sorted(recommendation_class.get_recommendations('test2')) == sorted(['test1'])
	assert sorted(recommendation_class.get_recommendations('test3')) == sorted(['test4'])
	assert sorted(recommendation_class.get_recommendations('test4')) == sorted(['test3'])
	assert recommendation_class.get_recommendations('test5') == 'User not found'
