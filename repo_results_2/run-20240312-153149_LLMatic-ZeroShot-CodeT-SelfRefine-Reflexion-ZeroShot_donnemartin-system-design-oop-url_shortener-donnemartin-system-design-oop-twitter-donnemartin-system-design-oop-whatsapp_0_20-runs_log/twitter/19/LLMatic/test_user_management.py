import pytest
from user_management import User


def test_register():
	user = User('test@test.com', 'testuser', 'testpass')
	assert user.register() == 'User registered successfully'


def test_authenticate():
	user = User('test@test.com', 'testuser', 'testpass')
	user.register()
	assert user.authenticate('testuser', 'testpass') == 'User authenticated successfully'
	assert user.authenticate('testuser', 'wrongpass') == 'Invalid username or password'


def test_reset_password():
	user = User('test@test.com', 'testuser', 'testpass')
	user.register()
	user.authenticate('testuser', 'testpass')
	assert user.reset_password('newpass') == 'Password reset successfully'
	assert user.authenticate('testuser', 'newpass') == 'User authenticated successfully'


def test_edit_profile():
	user = User('test@test.com', 'testuser', 'testpass')
	user.register()
	user.authenticate('testuser', 'testpass')
	assert user.edit_profile('newpic', 'newbio', 'newlink', 'newloc') == 'Profile updated successfully'


def test_toggle_profile_visibility():
	user = User('test@test.com', 'testuser', 'testpass')
	user.register()
	user.authenticate('testuser', 'testpass')
	assert user.toggle_profile_visibility() == 'Profile visibility toggled'


def test_follow():
	user1 = User('test1@test.com', 'testuser1', 'testpass')
	user2 = User('test2@test.com', 'testuser2', 'testpass')
	user1.register()
	user2.register()
	assert user1.follow('testuser2') == 'Followed testuser2'
	assert 'testuser1' in user2.get_followers()


def test_unfollow():
	user1 = User('test1@test.com', 'testuser1', 'testpass')
	user2 = User('test2@test.com', 'testuser2', 'testpass')
	user1.register()
	user2.register()
	user1.follow('testuser2')
	assert user1.unfollow('testuser2') == 'Unfollowed testuser2'
	assert 'testuser1' not in user2.get_followers()


def test_post():
	user = User('test@test.com', 'testuser', 'testpass')
	user.register()
	assert user.post('Hello, world!') == 'Post created'


def test_block_user():
	user1 = User('test1@test.com', 'testuser1', 'testpass')
	user2 = User('test2@test.com', 'testuser2', 'testpass')
	user1.register()
	user2.register()
	assert user1.block_user('testuser2') == 'Blocked testuser2'


def test_unblock_user():
	user1 = User('test1@test.com', 'testuser1', 'testpass')
	user2 = User('test2@test.com', 'testuser2', 'testpass')
	user1.register()
	user2.register()
	user1.block_user('testuser2')
	assert user1.unblock_user('testuser2') == 'Unblocked testuser2'


def test_send_message():
	user1 = User('test1@test.com', 'testuser1', 'testpass')
	user2 = User('test2@test.com', 'testuser2', 'testpass')
	user1.register()
	user2.register()
	assert user1.send_message('testuser2', 'Hello!') == 'Message sent'


def test_add_notification():
	user = User('test@test.com', 'testuser', 'testpass')
	user.register()
	assert user.add_notification('New follower') == 'Notification added'


def test_remove_notification():
	user = User('test@test.com', 'testuser', 'testpass')
	user.register()
	user.add_notification('New follower')
	assert user.remove_notification('New follower') == 'Notification removed'


def test_get_notifications():
	user = User('test@test.com', 'testuser', 'testpass')
	user.register()
	user.add_notification('New follower')
	assert 'New follower' in user.get_notifications()
