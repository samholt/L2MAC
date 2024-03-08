import pytest
from user import User

def test_user():
	user = User('test_user', 'password')
	assert user.username == 'test_user', 'Username is not set correctly'
	assert user.password == 'password', 'Password is not set correctly'

	user.create_account('new_user', 'new_password')
	assert user.username == 'new_user', 'Username is not updated correctly'
	assert user.password == 'new_password', 'Password is not updated correctly'

	user.save_favorite_recipe('recipe1')
	assert 'recipe1' in user.favorite_recipes, 'Favorite recipe is not saved correctly'

	user.follow_user('user2')
	assert 'user2' in user.followed_users, 'Followed user is not added correctly'

	user.add_activity('activity1')
	assert 'activity1' in user.activities, 'Activity is not added correctly'

	following = user.get_following()
	assert following == ['user2'], 'Following users are not returned correctly'

	activity = user.get_recent_activity()
	assert activity == ['activity1'], 'Recent activities are not returned correctly'

	user.set_preferences(['vegan', 'gluten-free'])
	preferences = user.get_preferences()
	assert preferences == ['vegan', 'gluten-free'], 'Preferences are not set correctly'
