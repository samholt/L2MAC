import pytest
from user_management import User
from social_interaction import SocialInteraction

def test_social_interaction():
    user1 = User()
    user1.register('user1', 'password1', 'user1@example.com')
    user2 = User()
    user2.register('user2', 'password2', 'user2@example.com')
    social_interaction = SocialInteraction()
    social_interaction.follow_user(user2)
    assert user2 in social_interaction.following
    social_interaction.unfollow_user(user2)
    assert user2 not in social_interaction.following
    assert social_interaction.view_timeline() == social_interaction.timeline
    social_interaction.send_message(user2, 'Hello')
    assert social_interaction.messages[user2] == 'Hello'
    social_interaction.receive_notification('New follower')
    assert 'New follower' in social_interaction.notifications