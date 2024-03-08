import pytest
from user import register_user, follow_user, get_user_recommendations

def test_user_recommendations():
	register_user('user1', 'user1@example.com', 'password1')
	register_user('user2', 'user2@example.com', 'password2')
	register_user('user3', 'user3@example.com', 'password3')
	follow_user('user1@example.com', 2)
	follow_user('user1@example.com', 3)
	follow_user('user2@example.com', 3)
	recommendations = get_user_recommendations(1)
	assert len(recommendations) == 1
	assert recommendations[0].id == 2
