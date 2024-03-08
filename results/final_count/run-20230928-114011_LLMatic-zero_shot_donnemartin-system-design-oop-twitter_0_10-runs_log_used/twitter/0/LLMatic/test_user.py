import pytest
from user import User
from post import Post


def test_register():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert user.register() == 'User registered successfully'


def test_authenticate():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert 'Invalid password' == user.authenticate('wrongpass')
	assert isinstance(user.authenticate('testpass'), str)


def test_reset_password():
	user = User('test@test.com', 'testuser', 'testpass', False)
	user.reset_password('newpass')
	assert 'Invalid password' == user.authenticate('testpass')
	assert isinstance(user.authenticate('newpass'), str)


def test_update_profile():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert user.update_profile(profile_picture='newpic.jpg', bio='new bio', website_link='newwebsite.com', location='new location') == 'Profile updated successfully'
	assert user.profile_picture == 'newpic.jpg'
	assert user.bio == 'new bio'
	assert user.website_link == 'newwebsite.com'
	assert user.location == 'new location'


def test_toggle_privacy():
	user = User('test@test.com', 'testuser', 'testpass', False)
	user.toggle_privacy()
	assert user.is_private == True
	user.toggle_privacy()
	assert user.is_private == False


def test_follow_unfollow():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	assert user1.follow(user2) == 'Followed successfully'
	assert user2 in user1.following
	assert user1 in user2.followers
	assert user1.unfollow(user2) == 'Unfollowed successfully'
	assert user2 not in user1.following
	assert user1 not in user2.followers


def test_notify_new_follower():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	assert user1.follow(user2) == 'Followed successfully'
	assert user2.notify_new_follower(user1) == 'New follower: testuser1'


def test_notify_like():
	user = User('test@test.com', 'testuser', 'testpass', False)
	post = Post(user, 'testpost')
	assert user.notify_like(post) == f'Your post was liked: {post.id}'


def test_notify_retweet():
	user = User('test@test.com', 'testuser', 'testpass', False)
	post = Post(user, 'testpost')
	assert user.notify_retweet(post) == f'Your post was retweeted: {post.id}'


def test_notify_reply():
	user = User('test@test.com', 'testuser', 'testpass', False)
	post = Post(user, 'testpost')
	assert user.notify_reply(post) == f'You received a reply on your post: {post.id}'


def test_notify_mention():
	user = User('test@test.com', 'testuser', 'testpass', False)
	post = Post(user, 'testpost')
	assert user.notify_mention(post) == f'You were mentioned in a post: {post.id}'


def test_recommend_users():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert user.recommend_users() == 'Recommended users'
