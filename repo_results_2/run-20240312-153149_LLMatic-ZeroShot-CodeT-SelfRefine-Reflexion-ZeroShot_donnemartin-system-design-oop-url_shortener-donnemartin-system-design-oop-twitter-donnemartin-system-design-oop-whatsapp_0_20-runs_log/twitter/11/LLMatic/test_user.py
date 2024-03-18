import pytest
from user import User
from post import Post

def test_register():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert user.register() == user

def test_authenticate():
	user = User('test@test.com', 'testuser', 'testpass', False)
	assert user.authenticate('testpass') is not False

def test_reset_password():
	user = User('test@test.com', 'testuser', 'testpass', False)
	user.reset_password('newpass')
	assert user.password == 'newpass'

def test_set_profile_picture():
	user = User('test@test.com', 'testuser', 'testpass', False)
	user.set_profile_picture('picture.jpg')
	assert user.profile_picture == 'picture.jpg'

def test_set_bio():
	user = User('test@test.com', 'testuser', 'testpass', False)
	user.set_bio('This is a bio')
	assert user.bio == 'This is a bio'

def test_set_website_link():
	user = User('test@test.com', 'testuser', 'testpass', False)
	user.set_website_link('www.example.com')
	assert user.website_link == 'www.example.com'

def test_set_location():
	user = User('test@test.com', 'testuser', 'testpass', False)
	user.set_location('New York')
	assert user.location == 'New York'

def test_toggle_privacy():
	user = User('test@test.com', 'testuser', 'testpass', False)
	user.toggle_privacy()
	assert user.is_private == True

def test_follow():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	assert user1.follow(user2) == 'Followed'
	assert user2 in user1.following
	assert user1 in user2.followers
	assert f'{user1.username} started following you.' in user2.notifications

def test_unfollow():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	user1.follow(user2)
	assert user1.unfollow(user2) == 'Unfollowed'
	assert user2 not in user1.following
	assert user1 not in user2.followers

def test_view_timeline():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	user1.follow(user2)
	assert user2.username in user1.view_timeline()

def test_notify_like():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	post = Post(user2, 'Hello, world!')
	user1.notify_like(post)
	assert f'{user1.username} liked your post: {post.text}' in user2.notifications

def test_notify_retweet():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	post = Post(user2, 'Hello, world!')
	user1.notify_retweet(post)
	assert f'{user1.username} retweeted your post: {post.text}' in user2.notifications

def test_notify_reply():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	post = Post(user2, 'Hello, world!')
	reply = Post(user1, 'Hello back!')
	user1.notify_reply(post, reply)
	assert f'{user1.username} replied to your post: {post.text} with {reply.text}' in user2.notifications

def test_notify_mention():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	post = Post(user1, f'Hello, {user2.username}!', mentions=[user2])
	user1.notify_mention(post)
	assert f'{user1.username} mentioned you in a post: {post.text}' in user2.notifications

def test_recommend_users():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	user3 = User('test3@test.com', 'testuser3', 'testpass', False)
	user4 = User('test4@test.com', 'testuser4', 'testpass', False)
	user1.follow(user2)
	user2.follow(user3)
	user2.follow(user4)
	user3.follow(user2)
	user4.follow(user2)
	recommended_users = user1.recommend_users([user3, user4])
	assert user3 in recommended_users
	assert user4 in recommended_users

