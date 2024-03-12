import pytest
from user import User

def test_get_user_recommendations():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	user3 = User('user3', 'password3')
	user4 = User('user4', 'password4')

	user1.follow_user(user2)
	user2.follow_user(user3)
	user3.follow_user(user4)

	recommendations = user1.get_user_recommendations()
	assert len(recommendations) == 1
	assert user3 in recommendations
