import pytest
from user import User, Profile


def test_user_methods():
	user1 = User('testuser1', 'testpassword1')
	user2 = User('testuser2', 'testpassword2')
	user1.submit_recipe({'name': 'recipe1', 'timestamp': '2022-01-01'})
	user1.favorite_recipe('recipe2')
	user1.remove_favorite_recipe('recipe2')
	user1.change_password('newpassword1')
	user1.follow_user(user2)
	user1.unfollow_user(user2)
	user1.update_activity_feed()
	assert user1.username == 'testuser1'
	assert user1.password == 'newpassword1'
	assert user1.submitted_recipes == [{'name': 'recipe1', 'timestamp': '2022-01-01'}]
	assert user1.favorite_recipes == []
	assert user1.following == []
	assert user1.activity_feed == []


def test_profile_methods():
	user = User('testuser', 'testpassword')
	profile = Profile(user)
	user.submit_recipe({'name': 'recipe1', 'timestamp': '2022-01-01'})
	user.favorite_recipe('recipe2')
	user.follow_user(User('testuser2', 'testpassword2'))
	assert profile.display_submitted_recipes() == [{'name': 'recipe1', 'timestamp': '2022-01-01'}]
	assert profile.display_favorite_recipes() == ['recipe2']
	assert len(profile.display_following()) == 1
	assert profile.display_activity_feed() == []
